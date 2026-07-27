<div align="center">

# Disuza Quantitative

### Public Technical Reference

Private pre-deployment quantitative R&D initiative

Version 4.0.0 · 2026-07-27

[![Pre-deployment R&D](https://img.shields.io/badge/status-Pre--deployment_R%26D-informational)](PUBLIC_FACTS.yml)
[![License: CC BY 4.0](https://img.shields.io/badge/license-CC_BY_4.0-lightgrey.svg)](LICENSE)
[![Last commit](https://img.shields.io/github/last-commit/DisuzaQuantitative/Disuza-Quantitative)](https://github.com/DisuzaQuantitative/Disuza-Quantitative/commits/main)

[Website](https://disuza.com) ·
[LinkedIn](https://www.linkedin.com/company/disuza-quantitative/) ·
[Public facts](PUBLIC_FACTS.yml) ·
[Documentation](docs/README.md)

</div>

---

> **Informational documentation only.** Nothing in this repository is
> investment advice, an offer, a solicitation, or a representation of legal
> registration, regulatory authorization, live deployment, trading activity,
> or investment performance.

## CURRENT — what Disuza Quantitative is

Disuza Quantitative is a private, pre-deployment quantitative R&D initiative
building and validating rule-based systematic trading infrastructure. Its
present work concerns research governance, validation discipline, software
design, and the controlled development of a systematic research stack.

This repository is the initiative's public documentation surface. It does not
contain a production trading platform, proprietary source code, model weights,
credentials, private datasets, or a performance record.

## Status vocabulary

Every architecture or capability statement in this repository must use one of
these labels:

| Label | Meaning |
| --- | --- |
| **CURRENT** | Publicly supportable state at the date shown in the document. |
| **IN PROGRESS** | Work is being designed, implemented, or evaluated; completion is not claimed. |
| **TARGET** | Intended future state; not a statement of present capability. |

The machine-readable source for these definitions and the repository's current
positioning is [`PUBLIC_FACTS.yml`](PUBLIC_FACTS.yml).

## Public status snapshot

- **CURRENT** — a private quantitative R&D initiative, a documentation and
  governance corpus, and research tooling under controlled development.
- **IN PROGRESS** — validation controls, data and execution abstractions, risk
  controls, and their supporting software are being developed and evaluated.
- **TARGET** — an auditable, deployment-ready systematic research and execution
  stack, subject to explicit qualification gates.

Descriptions of a target architecture do not imply that its components are
integrated, deployed, connected to capital, or operating in markets.

## Research scope and method

- **CURRENT** — the core research scope covers BTC and ETH perpetual markets
  and NQ and ES index-futures markets.
- **CURRENT** — optional CFD adaptations are evaluated as a separate research
  lane.
- **CURRENT** — the primary design horizon is approximately 30 minutes to
  4 hours.
- **CURRENT** — primary signal generation is rule-based. Machine learning may
  be evaluated only in auxiliary roles and only after the related hard-rule
  baseline qualifies out of sample.
- **CURRENT** — the public methodology includes temporal separation,
  pre-registration, cumulative trial accounting, CPCV, DSR, PBO, sanity
  checks, and reproducibility controls.

These methods reduce avoidable research error. They do not establish economic
value or future performance.

## Explicit non-claims

This repository makes no claim of:

- No live, production, paper-trading, or customer-facing operation is
  represented.
- No deployed execution, custody, managed account, or capital-management
  activity is represented.
- No historical or expected return, validated alpha, or
  investment-performance claim is made.
- No investment service, investment advice, financial product, offer, or
  solicitation is made.
- No legal incorporation, registration, licence, regulatory approval, or
  authorization is represented.

Research methodology can reduce avoidable error; it cannot establish future
performance.

## Documentation map

| Section | Scope |
| --- | --- |
| [Documentation index](docs/README.md) | Reading order and status conventions |
| [Public status](docs/status.md) | Current work, controls in progress, and target direction |
| [Overview](docs/overview.md) | Initiative scope and public boundaries |
| [Research methodology](docs/research-methodology.md) | Rule-based policy and anti-overfit controls |
| [Architecture](docs/architecture.md) | Current, in-progress, and target system views |
| [Components](docs/components.md) | Component responsibilities and status |
| [Data pipeline](docs/data-pipeline.md) | Data-quality and lineage design |
| [Execution](docs/execution.md) | Execution-control design, not live execution |
| [Risk](docs/risk.md) | Research and operational risk controls |
| [Operations](docs/operations.md) | Pre-deployment operational readiness |
| [Technology](docs/technology.md) | Tools used or evaluated in R&D |
| [Regulatory](docs/regulatory.md) | Public disclaimers and non-claims |
| [FAQ](docs/faq.md) | Short answers about scope and status |
| [Team](docs/team.md) | Public project roles |
| [Downstream alignment](docs/downstream-alignment-checklist.md) | Post-release checklist for surfaces excluded from v4.0.0 |

## Repository boundaries

The public repository intentionally stays at a documentation-safe level. It
must not include secrets, private identifiers, detailed control thresholds,
private infrastructure coordinates, proprietary algorithms, or unpublished
research results. See [`CONTRIBUTING.md`](CONTRIBUTING.md) for the publication
rules.

## Contact

General inquiries: [contact@disuza.com](mailto:contact@disuza.com).

## Licence

Unless a file says otherwise, the current public documentation is licensed
under [Creative Commons Attribution 4.0 International](LICENSE). Historical
licence grants remain valid for the exact material and versions to which they
were originally applied; see [`NOTICE.md`](NOTICE.md).

---

<div align="center">

Disuza Quantitative · Public Technical Reference · v4.0.0

Last updated: 2026-07-27

</div>

<!--
  status: CURRENT
  lifecycle: pre-deployment
  version: 4.0.0
  last_updated: 2026-07-27
  canonical_repository: https://github.com/DisuzaQuantitative/Disuza-Quantitative
-->
