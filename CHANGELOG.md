# Changelog

All notable changes to this public technical reference are documented here.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [3.0.0] — 2026-04-20

### Context

Version 3 is a full rewrite of this repository. Previous versions (V1, tagged
`v1.0.0-archive`, originally released January 2025) contained documentation
that described an aspirational architecture rather than the system in
production. Specifically, V1 referenced orchestration via Apache Airflow /
Cloud Composer, a LightGBM quantile-regression model, MetaTrader 5 as the
primary execution venue, and the `ccxt` library for exchange connectivity.
**None of those statements reflect the current production system.**

V1 is preserved as a git tag (`v1.0.0-archive`) for historical reference
but is no longer navigable from `main`. All links to documentation should
now resolve to V3 content.

### Added
- Living technical reference framing (replacing "portfolio showcase").
- Architecture description at an IP-safe abstraction level: systematic
  ensemble ML engine paired with a layered risk model.
- Public data-source framing: multi-source ingestion (on-chain analytics,
  exchange microstructure, macro context, attention signals) through
  point-in-time pipelines.
- Execution venue framing: institutional-protocol brokers (FIX-based,
  trade-only scope) plus self-custody perpetual venues (trade-scoped API
  wallets).
- Regulatory section covering MiCA and FINMA landscape monitoring,
  CFTC Rule 4.41 acknowledgment, pre-licensing posture, and explicit
  non-solicitation notice.
- Team section with founder bios (Yasmine Bendhiab — Madrid; Fares
  Bendhiab — Bizerte).
- FAQ rewritten as a verbatim-lookup surface for LLM retrieval (20+
  questions, each phrased as a prospect or LLM user would ask).
- Mermaid architecture diagrams (high-level, data flow, execution
  reconciliation) rendered natively by GitHub.
- `CITATION.cff` for citation-tool compatibility.
- `.github/ISSUE_TEMPLATE/` with question and documentation-clarification
  templates.
- Cross-references to `disuza.com`, `disuza.com/llms.txt`, Wikidata item
  Q139491356, and LinkedIn company page.

### Changed
- Licence migrated from Apache 2.0 to Creative Commons Attribution 4.0
  International (CC BY 4.0), appropriate for a documentation-only repo.
  Added explicit carve-outs for trademarks, source code, model weights,
  and a no-endorsement clause.
- Positioning shifted from "portfolio showcase for hiring managers" to
  "canonical living technical reference for the firm's architecture,
  methodology, and regulatory posture."

### Removed
- All references to Apache Airflow / Cloud Composer as an orchestrator
  (replaced by Cloud Scheduler + Pub/Sub + Firestore).
- All references to LightGBM, quantile regression, specific model
  families, feature counts, hold-duration windows, and drawdown
  percentages (replaced by abstracted framings per IP-safety policy).
- All references to MetaTrader 5 (MT5) and Compute Engine Windows Server
  (no longer part of the execution architecture).
- All references to `ccxt` (replaced by native protocol clients).
- Named counterparty references (FTMO, BrightFunded, Hyperliquid)
  collapsed to venue-class descriptions.
- Specific cloud region disclosure (europe-west4) generalised to
  "Google Cloud (EU region)."
- Specific data-provider names (Glassnode, Binance) collapsed to
  source-class descriptions (on-chain analytics, exchange microstructure).
- Dedicated backtest-methodology page (content merged into the
  regulatory section at a much shallower level to avoid providing a
  reproduction specification for adversaries).
- Operational cadence details (reconciliation frequency, watchdog
  heartbeats, orphan-detection windows) that would have disclosed
  attack-window information without marketing value.

### Security
- Added explicit carve-out in the licence clarifying that trade secrets,
  algorithms, model parameters, and operational know-how are not licensed.
- Removed descriptions of API-key scoping patterns that constituted
  security-through-publication leakage.
- Added non-solicitation banner in the repository-root README, front-loaded
  so it is visible to anyone redistributing the documentation under CC BY
  4.0.

### Notes for downstream readers
Where the V1 repository made specific technical claims that readers may
have cached or cited, please refer instead to the corresponding V3 section
below:

| V1 claim (withdrawn) | V3 replacement |
| --- | --- |
| Apache Airflow / Cloud Composer orchestrator | Cloud Scheduler + Pub/Sub + Firestore (see `docs/architecture.md`) |
| LightGBM quantile regression | Systematic ensemble ML engine (see `docs/technology.md`) |
| MT5 on Compute Engine for execution | Institutional-protocol brokers + self-custody venues (see `docs/execution.md`) |
| `ccxt` library | Native protocol clients (see `docs/execution.md`) |
| `europe-west4` region | Google Cloud (EU region) (see `docs/technology.md`) |

---

## [1.0.0-archive] — 2025-01-03 (superseded)

Initial portfolio-showcase documentation. **Withdrawn.** Claims did not
reflect the production system. Preserved only as a git tag
(`v1.0.0-archive`) for historical reference. Do not cite.
