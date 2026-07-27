#!/usr/bin/env python3
"""Fail closed on public-documentation drift and unsafe disclosures.

The checker intentionally uses only the Python standard library so contributors
can run it before installing any documentation tooling. Full CFF, Markdown,
external-link, Mermaid, and secret validation run as separate CI steps.
"""

from __future__ import annotations

import datetime as dt
import html
import re
import sys
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import unquote


ROOT = Path(__file__).resolve().parents[1]
EXPECTED_VERSION = "4.0.0"
FACTS_PATH = ROOT / "PUBLIC_FACTS.yml"
CHANGELOG_PATH = ROOT / "CHANGELOG.md"
TEXT_SUFFIXES = {
    ".cff",
    ".json",
    ".jsonc",
    ".md",
    ".mmd",
    ".py",
    ".sh",
    ".toml",
    ".txt",
    ".yaml",
    ".yml",
}
STATUS_LABELS = {"CURRENT", "IN PROGRESS", "TARGET"}


@dataclass(frozen=True, order=True)
class Issue:
    path: str
    line: int
    code: str
    message: str


issues: list[Issue] = []


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def add_issue(path: Path, line: int, code: str, message: str) -> None:
    issues.append(Issue(relative(path), line, code, message))


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def public_text_files() -> list[Path]:
    result: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if path.name != "LICENSE" and path.suffix.lower() not in TEXT_SUFFIXES:
            continue
        if any(part in {".git", "node_modules"} for part in path.parts):
            continue
        result.append(path)
    return sorted(result)


def strip_yaml_scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        value = value[1:-1]
    return value


def normalized_whitespace(value: str) -> str:
    return " ".join(value.split()).casefold()


def normalized_claim(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.casefold()).strip()


def simple_yaml_scalars(path: Path) -> dict[str, str]:
    """Read scalar mappings from the conservative YAML subset used here."""

    scalars: dict[str, str] = {}
    stack: list[tuple[int, str]] = []
    key_pattern = re.compile(
        r"""^(\s*)(?:"([^"]+)"|'([^']+)'|([A-Za-z0-9_-]+)):(?:\s*(.*))?$"""
    )

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith(("#", "- ")):
            continue
        match = key_pattern.match(raw_line)
        if not match:
            continue

        indent = len(match.group(1))
        key = match.group(2) or match.group(3) or match.group(4)
        value = (match.group(5) or "").strip()
        while stack and stack[-1][0] >= indent:
            stack.pop()
        dotted = ".".join([item[1] for item in stack] + [key])

        if value:
            scalars[dotted] = strip_yaml_scalar(value)
        else:
            stack.append((indent, key))

    return scalars


def simple_yaml_lists(path: Path) -> dict[str, list[str]]:
    """Read list items from the conservative YAML subset used here."""

    lists: dict[str, list[str]] = {}
    stack: list[tuple[int, str]] = []
    key_pattern = re.compile(
        r"""^(\s*)(?:"([^"]+)"|'([^']+)'|([A-Za-z0-9_-]+)):(?:\s*(.*))?$"""
    )
    item_pattern = re.compile(r"^(\s*)-\s+(.+?)\s*$")

    for raw_line in path.read_text(encoding="utf-8").splitlines():
        if not raw_line.strip() or raw_line.lstrip().startswith("#"):
            continue

        key_match = key_pattern.match(raw_line)
        if key_match:
            indent = len(key_match.group(1))
            key = key_match.group(2) or key_match.group(3) or key_match.group(4)
            value = (key_match.group(5) or "").strip()
            while stack and stack[-1][0] >= indent:
                stack.pop()
            if not value:
                stack.append((indent, key))
            continue

        item_match = item_pattern.match(raw_line)
        if not item_match or not stack:
            continue
        indent = len(item_match.group(1))
        while stack and stack[-1][0] >= indent:
            stack.pop()
        if not stack:
            continue
        dotted = ".".join(item[1] for item in stack)
        lists.setdefault(dotted, []).append(strip_yaml_scalar(item_match.group(2)))

    return lists


def require_file(path: Path) -> bool:
    if path.is_file():
        return True
    add_issue(path, 1, "missing-file", "required public-release file is missing")
    return False


def check_facts() -> tuple[str, str, dict[str, str], dict[str, list[str]]]:
    if not require_file(FACTS_PATH):
        return EXPECTED_VERSION, "", {}, {}

    facts = simple_yaml_scalars(FACTS_PATH)
    fact_lists = simple_yaml_lists(FACTS_PATH)
    required = {
        "document.version",
        "document.last_updated",
        "document.canonical_repository",
        "initiative.name",
        "initiative.positioning",
        "initiative.lifecycle",
        "status_vocabulary.CURRENT",
        "status_vocabulary.IN PROGRESS",
        "status_vocabulary.TARGET",
        "licensing.current_material",
        "contact.email",
    }
    for key in sorted(required - facts.keys()):
        add_issue(FACTS_PATH, 1, "facts-field", f"missing scalar field: {key}")

    required_lists = {
        "public_status.CURRENT",
        "public_status.IN PROGRESS",
        "public_status.TARGET",
        "capabilities.CURRENT",
        "capabilities.IN PROGRESS",
        "capabilities.TARGET",
        "target_architecture.components",
        "research_scope.core_markets",
        "research_scope.optional_research",
        "methodology.public_methods",
        "repository_scope.included",
        "repository_scope.excluded",
        "explicit_non_claims",
    }
    for key in sorted(required_lists):
        if not fact_lists.get(key):
            add_issue(FACTS_PATH, 1, "facts-list", f"missing or empty list: {key}")

    if facts.get("target_architecture.status") != "TARGET":
        add_issue(
            FACTS_PATH,
            1,
            "facts-architecture",
            "target_architecture.status must be TARGET",
        )
    if facts.get("target_architecture.deployment") != "not deployed":
        add_issue(
            FACTS_PATH,
            1,
            "facts-architecture",
            "target_architecture.deployment must be not deployed",
        )

    version = facts.get("document.version", "")
    release_date = facts.get("document.last_updated", "")

    if version != EXPECTED_VERSION:
        add_issue(
            FACTS_PATH,
            1,
            "facts-version",
            f"document.version must be {EXPECTED_VERSION}",
        )

    try:
        parsed_date = dt.date.fromisoformat(release_date)
    except ValueError:
        add_issue(
            FACTS_PATH,
            1,
            "facts-date",
            "document.last_updated must be an ISO date",
        )
    else:
        if parsed_date > dt.date.today():
            add_issue(
                FACTS_PATH,
                1,
                "facts-date",
                "document.last_updated cannot be in the future",
            )

    actual_statuses = {
        key.removeprefix("status_vocabulary.")
        for key in facts
        if key.startswith("status_vocabulary.")
    }
    if actual_statuses != STATUS_LABELS:
        add_issue(
            FACTS_PATH,
            1,
            "facts-statuses",
            "status_vocabulary must contain only CURRENT, IN PROGRESS, and TARGET",
        )

    return version, release_date, facts, fact_lists


def check_release_markers(version: str, release_date: str) -> None:
    marker_paths = [
        ROOT / "README.md",
        ROOT / "CONTRIBUTING.md",
        ROOT / ".github" / "profile" / "README.md",
        *sorted((ROOT / "docs").glob("*.md")),
    ]
    for path in marker_paths:
        if not require_file(path):
            continue
        text = path.read_text(encoding="utf-8")
        if version and version not in text:
            add_issue(path, 1, "release-version", "v4 release marker is missing")
        if release_date and release_date not in text:
            add_issue(path, 1, "release-date", "release date marker is missing")

    old_markers = (
        ("legacy-version", re.compile(r"(?i)\bv?3\.1(?:\.0)?\b")),
        ("legacy-date", re.compile(r"\b2026-05-" r"22\b")),
    )
    for path in public_text_files():
        if path == CHANGELOG_PATH:
            continue
        text = path.read_text(encoding="utf-8")
        for code, pattern in old_markers:
            for match in pattern.finditer(text):
                add_issue(
                    path,
                    line_number(text, match.start()),
                    code,
                    "legacy release marker is allowed only in CHANGELOG.md",
                )


def check_fact_consistency(
    version: str,
    release_date: str,
    facts: dict[str, str],
    fact_lists: dict[str, list[str]],
) -> None:
    name = facts.get("initiative.name", "")
    positioning = facts.get("initiative.positioning", "")
    lifecycle = facts.get("initiative.lifecycle", "")
    email = facts.get("contact.email", "")
    canonical_repository = facts.get("document.canonical_repository", "")

    for path in (
        ROOT / "README.md",
        ROOT / ".github" / "profile" / "README.md",
        ROOT / "docs" / "status.md",
        ROOT / "docs" / "faq.md",
    ):
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        for value, label in ((name, "initiative name"), (lifecycle, "lifecycle")):
            if value and value.casefold() not in text.casefold():
                add_issue(path, 1, "facts-consistency", f"missing {label} from PUBLIC_FACTS.yml")
        if positioning and normalized_whitespace(positioning) not in normalized_whitespace(text):
            add_issue(
                path,
                1,
                "facts-consistency",
                "canonical positioning must match PUBLIC_FACTS.yml verbatim",
            )

    for path in (ROOT / "README.md", ROOT / ".github" / "profile" / "README.md"):
        if path.is_file() and email:
            text = path.read_text(encoding="utf-8")
            if email.casefold() not in text.casefold():
                add_issue(path, 1, "facts-consistency", "missing public contact email")

    cff_path = ROOT / "CITATION.cff"
    if not require_file(cff_path):
        return
    cff = simple_yaml_scalars(cff_path)
    required_cff = {
        "cff-version",
        "message",
        "title",
        "url",
        "license",
        "version",
        "date-released",
    }
    for key in sorted(required_cff - cff.keys()):
        add_issue(cff_path, 1, "cff-field", f"missing top-level CFF field: {key}")

    expected_cff = {
        "cff-version": "1.2.0",
        "version": version,
        "date-released": release_date,
        "license": facts.get("licensing.current_material", ""),
        "url": canonical_repository,
    }
    for key, expected in expected_cff.items():
        if expected and cff.get(key) != expected:
            add_issue(cff_path, 1, "cff-consistency", f"{key} must match PUBLIC_FACTS.yml")

    cff_text = cff_path.read_text(encoding="utf-8")
    if name and name.casefold() not in cff_text.casefold():
        add_issue(cff_path, 1, "cff-consistency", "initiative name is missing")
    if positioning and normalized_whitespace(positioning) not in normalized_whitespace(cff_text):
        add_issue(
            cff_path,
            1,
            "cff-consistency",
            "canonical positioning must match PUBLIC_FACTS.yml verbatim",
        )
    if not re.search(r"(?m)^\s*-\s+name:\s*\S", cff_text):
        add_issue(cff_path, 1, "cff-authors", "at least one named author is required")

    projections = {
        "capabilities.CURRENT": [ROOT / "docs" / "skills.md"],
        "capabilities.IN PROGRESS": [ROOT / "docs" / "skills.md"],
        "capabilities.TARGET": [ROOT / "docs" / "skills.md"],
        "target_architecture.components": [ROOT / "docs" / "architecture.md"],
        "research_scope.core_markets": [
            ROOT / "README.md",
            ROOT / "docs" / "status.md",
            ROOT / "docs" / "faq.md",
        ],
        "research_scope.optional_research": [
            ROOT / "README.md",
            ROOT / "docs" / "status.md",
            ROOT / "docs" / "faq.md",
        ],
        "methodology.public_methods": [
            ROOT / "README.md",
            ROOT / "docs" / "research-methodology.md",
        ],
        "explicit_non_claims": [ROOT / "README.md"],
    }
    for key, paths in projections.items():
        corpus = normalized_claim(
            "\n".join(
                path.read_text(encoding="utf-8") for path in paths if path.is_file()
            )
        )
        for item in fact_lists.get(key, []):
            if normalized_claim(item) not in corpus:
                add_issue(
                    FACTS_PATH,
                    1,
                    "facts-projection",
                    f"{key} item is not projected into its canonical public page: {item}",
                )

    scalar_projections = {
        "research_scope.primary_horizon": [
            ROOT / "README.md",
            ROOT / "docs" / "status.md",
            ROOT / "docs" / "faq.md",
        ],
        "methodology.primary_signal_policy": [
            ROOT / "README.md",
            ROOT / "docs" / "research-methodology.md",
            ROOT / "docs" / "faq.md",
        ],
    }
    for key, paths in scalar_projections.items():
        expected = facts.get(key, "")
        corpus = normalized_claim(
            "\n".join(
                path.read_text(encoding="utf-8") for path in paths if path.is_file()
            )
        )
        if expected and normalized_claim(expected) not in corpus:
            add_issue(
                FACTS_PATH,
                1,
                "facts-projection",
                f"{key} is not projected into its canonical public page",
            )


FORBIDDEN_RULES = (
    (
        "internal-id",
        re.compile(r"(?i)\b(?:D|S|H)(?:[_-]?\d{2,})\b"),
        "internal research or decision identifier",
    ),
    (
        "internal-gate",
        re.compile(r"(?i)\bgate\s*\d+\b"),
        "internal gate identifier",
    ),
    (
        "private-key",
        re.compile(r"-----BEGIN (?:[A-Z0-9 ]+ )?PRIVATE KEY-----"),
        "private-key material",
    ),
    (
        "credential-value",
        re.compile(
            r"""(?ix)
            \b(?:api[_ -]?key|access[_ -]?token|password|private[_ -]?key|secret)
            \b\s*[:=]\s*["']?[A-Za-z0-9_./+=-]{8,}
            """
        ),
        "credential-like assignment",
    ),
    (
        "cloud-role",
        re.compile(
            r"(?i)\b(?:roles/[a-z][\w.]+|service"
            r"Account:\S+|\bI"
            r"AM\b)"
        ),
        "private authorization detail",
    ),
    (
        "service-account",
        re.compile(r"(?i)\bservice" r"\s+accounts?\b"),
        "private runtime identity detail",
    ),
    (
        "storage-locator",
        re.compile(r"(?i)\b(?:gs|s3)://\S+"),
        "private storage locator",
    ),
    (
        "cloud-region",
        re.compile(
            r"(?i)\b(?:asia|australia|europe|me|northamerica|southamerica|us)-"
            r"(?:central|east|west|north|south|northeast|southeast)\d\b"
        ),
        "specific infrastructure region",
    ),
    (
        "private-path",
        re.compile(r"(?i)(?<![:\w])/(?:Users|home|data|mnt|srv|var)/[^\s`\"']+"),
        "private absolute data or host path",
    ),
    (
        "content-hash",
        re.compile(r"(?i)\b(?:sha(?:1|256|512)?\s*[:=]\s*)[0-9a-f]{12,}\b"),
        "private content hash",
    ),
    (
        "repository-sha",
        re.compile(r"(?i)\b[0-9a-f]{40}\b"),
        "repository commit identifier",
    ),
    (
        "private-counterparty",
        re.compile(
            r"""(?ix)
            \b(?:broker|counterparty|data[_ -]?provider|execution[_ -]?venue)
            \b\s*[:=]\s*["']?[A-Za-z0-9][A-Za-z0-9_.-]{2,}
            """
        ),
        "named provider, venue, broker, or counterparty",
    ),
    (
        "numeric-control",
        re.compile(
            r"""(?ix)
            \b(?:threshold|drawdown|exposure|stop|timeout|heartbeat)
            \b[^\n]{0,24}\b\d+(?:\.\d+)?\s*(?:%|bps?|seconds?|minutes?|hours?|days?)\b
            """
        ),
        "specific operational control value",
    ),
    (
        "numbered-research-detail",
        re.compile(
            r"(?i)(?:\b\d+\s+(?:trials?|splits?)\b|"
            r"\b(?:trials?|splits?)\s*[:=]\s*\d+\b)"
        ),
        "specific trial or split count",
    ),
    (
        "numeric-performance",
        re.compile(
            r"""(?ix)
            (?:
              \b(?:alpha|performance|profit|return(?:ed|s)|sharpe)
              \b[^\n]{0,32}
              |
              \breturn\b\s*(?:of|was|is|:|=)\s*
            )
            \b[-+]?\d+(?:\.\d+)?\s*(?:%|percent|x)?
            """
        ),
        "numeric research or performance result",
    ),
    (
        "numeric-percent",
        re.compile(r"(?<![A-Za-z0-9])[-+]?\d+(?:\.\d+)?\s*%"),
        "specific percentage value",
    ),
    (
        "operational-cadence",
        re.compile(
            r"""(?ix)
            \b(?:checks?|executes?|polls?|reconciles?|refreshes?|runs?|updates?)
            \b[^\n]{0,24}\bevery\s+\d+(?:\.\d+)?\s*
            (?:seconds?|minutes?|hours?|days?)\b
            """
        ),
        "specific operational cadence",
    ),
    (
        "contextual-hash",
        re.compile(
            r"""(?ix)
            \b(?:artifact|commit|content|data(?:set)?|repository)[_ -]?hash
            \b\s*[:=]\s*["']?[0-9a-f]{12,128}\b
            """
        ),
        "private content or repository hash",
    ),
    (
        "named-research-detail",
        re.compile(
            r"""(?ix)
            \b(?:candidate|hypothesis|strategy)[_ -]?(?:code|id|name)
            \b\s*[:=]\s*["']?[A-Za-z0-9][A-Za-z0-9_.-]{2,}
            """
        ),
        "named private research item",
    ),
    (
        "affirmative-live-operation",
        re.compile(
            r"""(?ix)
            \b(?:disuza(?:\s+quantitative)?|initiative|platform|system|we)
            \b[^\n.!?]{0,24}
            \b(?:am|are|is|operates?|runs?|trades?)
            \b[^\n.!?]{0,32}\b(?:live|production)\b
            """
        ),
        "affirmative live or production operation claim",
    ),
    (
        "affirmative-investment-service",
        re.compile(
            r"""(?ix)
            \b(?:disuza(?:\s+quantitative)?|initiative|platform|system|we)
            \b[^\n.!?]{0,24}
            \b(?:accepts?|manages?|offers?|provides?|sells?)
            \b[^\n.!?]{0,40}
            \b(?:capital|investment\s+(?:advice|services?)|managed\s+accounts?|signals?)
            \b
            """
        ),
        "affirmative investment, capital-management, or signal-service claim",
    ),
)


def check_forbidden_disclosures() -> None:
    for path in public_text_files():
        text = path.read_text(encoding="utf-8")
        for code, pattern, message in FORBIDDEN_RULES:
            for match in pattern.finditer(text):
                add_issue(path, line_number(text, match.start()), code, message)


def github_heading_anchors(text: str) -> set[str]:
    anchors: set[str] = set()
    duplicates: dict[str, int] = {}
    in_fence = False

    for line in text.splitlines():
        if re.match(r"^\s*(```|~~~)", line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue

        explicit = re.search(r"""<a\s+(?:name|id)=["']([^"']+)["']""", line, re.I)
        if explicit:
            anchors.add(explicit.group(1))

        match = re.match(r"^\s{0,3}#{1,6}\s+(.+?)\s*#*\s*$", line)
        if not match:
            continue
        heading = html.unescape(match.group(1))
        heading = re.sub(r"<[^>]+>", "", heading)
        heading = re.sub(r"[`*_~]", "", heading).strip().casefold()

        characters: list[str] = []
        for char in heading:
            category = unicodedata.category(char)
            if char in {"-", "_"} or char.isspace() or not category.startswith(("P", "S")):
                characters.append(char)
        base = re.sub(r"\s", "-", "".join(characters)).strip("-")
        number = duplicates.get(base, 0)
        duplicates[base] = number + 1
        anchors.add(base if number == 0 else f"{base}-{number}")

    return anchors


def markdown_links(path: Path) -> list[tuple[int, str]]:
    links: list[tuple[int, str]] = []
    pattern = re.compile(
        r"""!?\[[^\]]*\]\(\s*(?:<([^>]+)>|([^\s)]+))(?:\s+["'][^)]*)?\)"""
    )
    in_fence = False
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if re.match(r"^\s*(```|~~~)", line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        for match in pattern.finditer(line):
            links.append((number, match.group(1) or match.group(2)))
    return links


def check_relative_links() -> None:
    anchor_cache: dict[Path, set[str]] = {}
    markdown_paths = [
        path
        for path in public_text_files()
        if path.suffix.lower() == ".md" and path != CHANGELOG_PATH
    ]

    for source in markdown_paths:
        for number, raw_destination in markdown_links(source):
            destination = html.unescape(raw_destination).strip()
            if re.match(r"^[A-Za-z][A-Za-z0-9+.-]*:", destination):
                continue
            if destination.startswith("//"):
                continue

            file_part, separator, anchor = destination.partition("#")
            file_part = unquote(file_part.split("?", 1)[0])
            if file_part.startswith("/"):
                add_issue(
                    source,
                    number,
                    "absolute-link",
                    "repository links must be relative",
                )
                continue

            target = source if not file_part else (source.parent / file_part).resolve()
            try:
                target.relative_to(ROOT)
            except ValueError:
                add_issue(source, number, "escaping-link", "relative link escapes repository")
                continue

            if file_part and not target.is_file():
                add_issue(source, number, "broken-link", "relative link target does not exist")
                continue

            if separator and anchor:
                if target.suffix.lower() != ".md":
                    add_issue(
                        source,
                        number,
                        "invalid-anchor",
                        "anchors may target Markdown files only",
                    )
                    continue
                if target not in anchor_cache:
                    anchor_cache[target] = github_heading_anchors(
                        target.read_text(encoding="utf-8")
                    )
                if unquote(anchor).casefold() not in anchor_cache[target]:
                    add_issue(source, number, "broken-anchor", "Markdown anchor does not exist")


CAPABILITY_VERBS = re.compile(
    r"(?i)\b(?:builds?|building|develops?|deploys?|delivers?|executes?|"
    r"generates?|hosts?|includes?|integrates?|implements?|maintains?|manages?|"
    r"monitors?|operates?|places?|processes?|provides?|publishes?|"
    r"reconciles?|routes?|runs?|serves?|stores?|supports?|uses?|"
    r"validates?|validating)\b"
)
NON_CURRENT_CONTEXT = re.compile(
    r"(?i)\b(?:being|no|not|never|without|would|will|may|might|could|must|"
    r"intended|future|planned|targets?|doesn't|cannot|documentation|statement)\b"
)
DEPLOYMENT_TERMS = re.compile(r"(?i)\b(?:deployed|live|production)\b")
INSTRUCTION_BULLET = re.compile(
    r"^\s*(?:[-*+]\s+|\d+[.)]\s+)"
    r"(?:align|check|confirm|do|keep|prefer|record|remove|separate|use|verify)\b",
    re.I,
)


def status_in_text(text: str) -> str | None:
    found = {label for label in STATUS_LABELS if re.search(rf"\b{label}\b", text)}
    return next(iter(found)) if len(found) == 1 else None


def check_present_capability_claims() -> None:
    claim_paths = [
        path
        for path in public_text_files()
        if path.suffix.lower() == ".md" and path != CHANGELOG_PATH
    ]

    for path in claim_paths:
        if not path.is_file():
            continue
        section_status: dict[int, str | None] = {}
        in_fence = False
        in_html_comment = False
        paragraph_status: str | None = None
        paragraph_non_current = False

        for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
            if in_html_comment:
                if "-->" in line:
                    in_html_comment = False
                continue
            if "<!--" in line:
                if "-->" not in line.split("<!--", 1)[1]:
                    in_html_comment = True
                continue
            if re.match(r"^\s*(```|~~~)", line):
                in_fence = not in_fence
                continue
            if in_fence:
                continue
            if not line.strip():
                paragraph_status = None
                paragraph_non_current = False
                continue
            if re.match(r"^\s*(?:[-*+]\s+|\d+[.)]\s+|\|)", line):
                paragraph_status = None
                paragraph_non_current = False

            heading = re.match(r"^\s{0,3}(#{1,6})\s+(.+?)\s*#*\s*$", line)
            if heading:
                level = len(heading.group(1))
                for known_level in list(section_status):
                    if known_level >= level:
                        del section_status[known_level]
                inherited = section_status[max(section_status)] if section_status else None
                section_status[level] = status_in_text(heading.group(2)) or inherited
                paragraph_status = None
                paragraph_non_current = False
                continue

            if not CAPABILITY_VERBS.search(line):
                explicit = status_in_text(line)
                if explicit:
                    paragraph_status = explicit
                if NON_CURRENT_CONTEXT.search(line):
                    paragraph_non_current = True
                continue
            if INSTRUCTION_BULLET.search(line):
                continue
            explicit = status_in_text(line)
            if explicit:
                paragraph_status = explicit
            if NON_CURRENT_CONTEXT.search(line):
                paragraph_non_current = True
            if paragraph_non_current:
                continue

            active = explicit
            if active is None:
                active = paragraph_status
            if active is None and section_status:
                active = section_status[max(section_status)]
            if (
                DEPLOYMENT_TERMS.search(line)
                and not NON_CURRENT_CONTEXT.search(line)
                and active != "TARGET"
            ):
                add_issue(
                    path,
                    number,
                    "forbidden-deployment-claim",
                    "affirmative live, production, or deployed capability claim",
                )
            if active != "CURRENT":
                add_issue(
                    path,
                    number,
                    "unclassified-present-claim",
                    "present capability language must be classified CURRENT",
                )


def check_diagram_contract() -> None:
    diagrams_dir = ROOT / "docs" / "diagrams"
    diagrams = sorted(diagrams_dir.glob("*.mmd")) if diagrams_dir.is_dir() else []
    if diagrams:
        add_issue(
            diagrams_dir,
            1,
            "diagram-count",
            "standalone Mermaid sources are forbidden; embed the canonical block",
        )

    architecture = ROOT / "docs" / "architecture.md"
    if not require_file(architecture):
        return
    architecture_text = architecture.read_text(encoding="utf-8")
    blocks = re.findall(
        r"```mermaid\s*\n(.*?)\n```",
        architecture_text,
        flags=re.DOTALL,
    )
    if len(blocks) != 1:
        add_issue(
            architecture,
            1,
            "diagram-count",
            "architecture.md must contain exactly one Mermaid block",
        )
        return

    required_phrases = ("Target architecture", "not deployed", "TARGET")
    for phrase in required_phrases:
        if phrase.casefold() not in blocks[0].casefold():
            add_issue(
                architecture,
                1,
                "diagram-label",
                f"diagram must include: {phrase}",
            )


def main() -> int:
    version, release_date, facts, fact_lists = check_facts()
    check_release_markers(version, release_date)
    check_fact_consistency(version, release_date, facts, fact_lists)
    check_forbidden_disclosures()
    check_relative_links()
    check_present_capability_claims()
    check_diagram_contract()

    if issues:
        for issue in sorted(set(issues)):
            print(
                f"ERROR {issue.path}:{issue.line} "
                f"[{issue.code}] {issue.message}",
                file=sys.stderr,
            )
        print(f"Public-surface validation failed with {len(set(issues))} issue(s).", file=sys.stderr)
        return 1

    print(
        f"Public-surface validation passed for v{version} "
        f"(release date {release_date})."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
