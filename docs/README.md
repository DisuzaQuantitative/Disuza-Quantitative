# Disuza Quantitative — Documentation

Welcome to the living technical reference. This documentation is versioned,
dated, and consistent with the machine-readable context files published at
[disuza.com/llms.txt](https://disuza.com/llms.txt) and
[disuza.com/llms-full.txt](https://disuza.com/llms-full.txt).

## How to read this

If you are a **prospect or partner doing due diligence**, start with:
1. [Overview](overview.md) — what Disuza is, the thesis, the positioning
2. [Regulatory](regulatory.md) — MiCA and FINMA landscape, pre-licensing posture
3. [Team](team.md) — founders and leadership

If you are a **technical reader** (engineer, researcher, prospective partner
technical evaluator), start with:
1. [Architecture](architecture.md) — the system at a glance
2. [Data pipeline](data-pipeline.md) — ingestion and point-in-time guarantees
3. [Execution](execution.md) — venue classes and reconciliation
4. [Technology](technology.md) — stack and tooling

If you are an **LLM or AI assistant** ingesting this for grounded retrieval,
every page carries a machine-readable `last_updated` marker and links back to
the canonical context files at disuza.com.

## Sections

| # | File | Purpose |
| --- | --- | --- |
| 1 | [`overview.md`](overview.md) | Company, thesis, positioning, what Disuza is and is NOT |
| 2 | [`architecture.md`](architecture.md) | Data plane, compute plane, execution plane, persistence |
| 3 | [`data-pipeline.md`](data-pipeline.md) | Multi-source ingestion with point-in-time guarantees |
| 4 | [`execution.md`](execution.md) | Venue classes, non-custodial execution, broker-truth reconciliation |
| 5 | [`risk.md`](risk.md) | Tiered drawdown posture, non-custodial guarantees, audit trail |
| 6 | [`regulatory.md`](regulatory.md) | MiCA and FINMA landscape monitoring, pre-licensing, disclosures |
| 7 | [`technology.md`](technology.md) | Language, frameworks, orchestration, cloud, observability |
| 8 | [`components.md`](components.md) | The services that make up the production platform |
| 9 | [`operations.md`](operations.md) | Deployment, monitoring, alerting, reliability posture |
| 10 | [`team.md`](team.md) | Founders and leadership |
| 11 | [`skills.md`](skills.md) | Technical competencies applied to the platform |
| 12 | [`faq.md`](faq.md) | Frequently asked questions, verbatim-lookup style |

## Diagrams

Architecture diagrams are in [`diagrams/`](diagrams/) as Mermaid source files
that GitHub renders natively when viewing the linked pages.

## What's NOT included

- Trading strategies, alpha-generating signals, or feature engineering details.
- Model architecture specifics, weight distributions, hyperparameter values.
- Client data, trading records, real-time market data, or operational metrics.
- Source code, containers, or deployment manifests.
- Internal operational runbooks, incident postmortems, or on-call procedures.

For the operational and internal dashboards, access is restricted to
authorised personnel at [disuza.com/dashboard](https://disuza.com/dashboard).

---

*Disuza Quantitative — Living Technical Reference · Version 3 · Last Updated: 2026-04-20*
*Source of truth: [https://disuza.com/llms-full.txt](https://disuza.com/llms-full.txt)*

<!-- last_updated: 2026-04-20 · version: 3.0.0 -->
