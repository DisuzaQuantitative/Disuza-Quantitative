#!/usr/bin/env python3
"""Strict YAML validation for public release metadata."""

from __future__ import annotations

from pathlib import Path

import yaml
from yaml.constructor import ConstructorError


ROOT = Path(__file__).resolve().parents[1]
FILES = (ROOT / "PUBLIC_FACTS.yml", ROOT / "CITATION.cff")


class UniqueKeyLoader(yaml.SafeLoader):
    """Safe YAML loader that rejects duplicate mapping keys."""


def construct_unique_mapping(
    loader: UniqueKeyLoader,
    node: yaml.MappingNode,
    deep: bool = False,
) -> dict[object, object]:
    mapping: dict[object, object] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key in mapping:
            raise ConstructorError(
                "while constructing a mapping",
                node.start_mark,
                f"duplicate key: {key!r}",
                key_node.start_mark,
            )
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


UniqueKeyLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    construct_unique_mapping,
)


def main() -> int:
    for path in FILES:
        document = yaml.load(path.read_text(encoding="utf-8"), Loader=UniqueKeyLoader)
        if not isinstance(document, dict):
            raise TypeError(f"{path.name} must contain a top-level mapping")
    print("Strict YAML validation passed for PUBLIC_FACTS.yml and CITATION.cff.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
