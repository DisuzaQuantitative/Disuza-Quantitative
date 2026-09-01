# Overview

> **Version 4.0.0 candidate · Unreleased · Last verified 2026-09-01**

## CURRENT — initiative

Disuza Quantitative is a private, pre-deployment quantitative R&D initiative
building and validating rule-based systematic trading infrastructure. It is
founder-led across Madrid, Spain, and Bizerte, Tunisia.

Its present work is research and engineering: developing rule-based systematic
methods, testing their assumptions, strengthening research controls, and
building the foundations required for later qualification.

Forward-only market-data capture and monitoring are operational for research
data collection. They do not place orders, operate accounts, connect capital,
or constitute a trading runtime.

## CURRENT — programme research scope

The core market scope is:

- BTC and ETH perpetual markets;
- NQ and ES index-futures markets;
- optional CFD research as a separate adaptation lane.

The primary design horizon is approximately 30 minutes to 4 hours.

This scope describes what is researched. It does not state that these markets
are currently traded live.

It is programme research scope only, not qualified engine coverage. A bounded
execution-engine contract is qualified on deterministic synthetic fixtures only;
it has not processed market data, and its narrow contract does not establish
coverage of the programme research universe or design horizon.

## CURRENT — design position

The programme is:

- **rule-based first** — primary signals must come from explicit economic and
  market rules;
- **methodology-led** — hypotheses, trial accounting, temporal separation,
  reproducibility, and anti-overfit checks govern evaluation;
- **audit-oriented** — verified facts, judgment, and unknowns are kept
  separate;
- **private by design** — source code, strategies, datasets, and operational
  details are not published.

Machine learning is limited to auxiliary research roles and only after a
hard-rule baseline qualifies out of sample.

## IN PROGRESS — governance and integrity

The research programme is strengthening controls around access, trial
accounting, reproducibility, and independent audit evidence.

This is the current priority. The public reference therefore makes no current
strategy-performance claim and no trading-system deployment claim.

## TARGET — future system

The longer-term target is a qualified systematic trading system with:

- controlled paper and live execution paths;
- venue-appropriate risk controls;
- reconciled order and fill accounting;
- non-custodial design where applicable;
- explicit human approval at promotion boundaries.

These are target properties, not descriptions of a currently live platform.

## What Disuza Quantitative is not

Disuza Quantitative is not:

- a public hedge fund;
- a retail signal service;
- a provider of investment services through this repository;
- an invitation to invest;
- a claim of live or future performance;
- a high-frequency co-location operation.

## Leadership footprint

The initiative is led across Madrid and Bizerte. Public documentation uses a
neutral organisational voice and does not expose private working arrangements.

## Contact

General inquiries: **[contact@disuza.com](mailto:contact@disuza.com)**

See [`status.md`](status.md) for the current public status and
[`research-methodology.md`](research-methodology.md) for the research policy.

---

*Disuza Quantitative — Public Technical Reference · Version 4.0.0 candidate ·
Unreleased · Last verified 2026-09-01*
