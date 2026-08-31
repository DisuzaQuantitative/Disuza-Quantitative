# Changelog

Notable changes to the Disuza Quantitative Public Technical Reference are
recorded here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).
Release numbers describe this public documentation, not a trading system or
investment product.

## [4.0.0] — Unreleased

Last verified: 2026-09-01.

### Context

Version 4.0.0 resets the public reference around one canonical positioning:
Disuza Quantitative is a **private pre-deployment quantitative R&D
initiative**.

Architecture and capability descriptions now distinguish **CURRENT**,
**IN PROGRESS**, and **TARGET** state. A target description is not evidence of
deployment, integration, trading activity, or performance.

### Added

- `PUBLIC_FACTS.yml` as the machine-readable source for public positioning,
  lifecycle, status definitions, repository scope, and explicit non-claims.
- `NOTICE.md` for attribution, licence scope, and continuity of historical
  licence grants.
- `docs/status.md`, `docs/research-methodology.md`, and a separate downstream
  alignment checklist.
- Repository-wide status vocabulary for present state, active work, and
  intended future state.
- Explicit boundaries for information that must not be published.
- Read-only documentation CI for facts, claims, Markdown, links, anchors, CFF,
  Mermaid, and redacted secret scanning.

### Changed

- Reframed the root README, organization-profile mirror, citation metadata,
  and contribution policy around pre-deployment research and development.
- Reclassified architecture, data, execution, risk, technology, and operations
  descriptions by lifecycle status.
- Distinguished operational forward-only research data capture from any
  trading runtime, order placement, account operation, or capital connectivity.
- Recorded the bounded synthetic-fixture engine evidence without claiming
  market-data, strategy-performance, paper, live, or deployment qualification.
- Separated the current engine route's purged and embargoed anchored
  walk-forward plus DSR controls from CPCV and PBO programme methods that apply
  only where their evaluation geometry supports them.
- Corrected the public non-technical business, legal, and administrative role.
- Consolidated the architecture into one target-only Mermaid diagram and kept
  superseded documentation paths as one-major-version compatibility stubs.
- Rebuilt the 1200×630 Open Graph image around pre-deployment systematic
  trading R&D.
- Made CC BY 4.0 the canonical licence for the current public documentation.
- Reduced technical descriptions to a documentation-safe level.

### Removed

- Statements that could be read as claims of a live or production trading
  platform.
- Performance, returns, validated-alpha, managed-account, custody, capital, and
  investment-service claims.
- Claims of legal registration, licensing, regulatory approval, or
  authorization.
- Guest-portal links and references to historical performance artefacts.
- Private identifiers, control thresholds, infrastructure coordinates,
  proprietary implementation details, and unpublished research results.

### Licence continuity

The licence change is prospective for the current distribution. Rights already
granted under licence notices attached to earlier versions remain in effect for
the exact historical material covered by those notices. See `NOTICE.md`.

## [3.1.0] — 2026-05-22

### v4 preservation notice

This historical entry is retained as a disclosure-safe summary. Version 4.0.0
withdraws every v3.1 statement that could be read as current deployment,
platform, performance, investment, legal, or regulatory status. The exact
entry originally published with v3.1 remains available in the existing Git
history; its removal from current `main` is explicit rather than a silent
rewrite.

### Historical context

V3.1 was a corrective documentation release that:

- changed the stated primary research policy from model-led to rule-based,
  with machine learning limited to auxiliary research roles;
- added high-level anti-overfit methodology, temporal separation,
  pre-registration, trial accounting, and reproducibility language;
- added NQ and ES to the stated research scope;
- revised technology, data-source, execution-protocol, and calibration
  descriptions; and
- removed several superseded technology and data-class claims.

### Withdrawn v3.1 claims

- Historical performance and validation-artifact references are not current
  evidence and are not republished in v4.
- Statements implying a current platform direction, deployed execution, or
  operating infrastructure are withdrawn.
- Any architecture or capability surviving into v4 is restated independently
  under **CURRENT**, **IN PROGRESS**, or **TARGET**.

## [3.0.0] — 2026-04-20

### v4 preservation notice

V3.0 was a full rewrite of the earlier showcase. Its detailed architecture,
operating, legal, regulatory, and organizational language is superseded by
version 4.0.0. The exact original entry remains available in Git history for
provenance; v4 intentionally does not republish sensitive or unsupported
details from that entry.

### Historical scope

The v3.0 release introduced:

- a living-technical-reference format;
- high-level data, research, execution, and risk descriptions;
- founder biographies, FAQ, diagrams, citation metadata, and issue templates;
- cross-references to external identity surfaces; and
- an announced move toward CC BY 4.0 for documentation.

It also removed or generalized named technologies, providers, counterparties,
infrastructure locations, model details, control values, and operational
cadences from earlier public material.

### Withdrawn v3.0 claims

- The description of an existing production system is withdrawn.
- Model-led, live-execution, current-infrastructure, performance, legal-status,
  and regulatory-readiness language is not current.
- V3 diagrams and component descriptions are superseded by the single v4
  **TARGET — not deployed** architecture.
- Earlier licensing notices remain effective for the exact historical material
  to which they applied.

## [1.0.0-archive] — 2025-01-03

Archived initial documentation release. Its claims are withdrawn and it must
not be treated as a current description. The exact historical entry and
release remain available in Git history for provenance.
