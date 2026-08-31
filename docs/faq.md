# Frequently Asked Questions

> **Version 4.0.0 candidate · Unreleased · Last verified 2026-09-01**

## What is Disuza Quantitative?

**CURRENT:** Disuza Quantitative is a private, pre-deployment quantitative R&D initiative
building and validating rule-based systematic trading infrastructure.

## Where is the initiative led?

The initiative is led across Madrid, Spain, and Bizerte, Tunisia.

## What is the current stage?

- **CURRENT:** research and engineering.
- **IN PROGRESS:** stronger integrity, access, trial-accounting, and audit
  controls.
- **TARGET:** qualified paper and live deployment after the required evidence
  and approvals exist.

## Is there a live trading platform?

No live trading platform is represented. Forward-only market-data capture and
monitoring are operational for research data collection, but they do not place
orders, operate accounts, connect capital, or constitute a trading runtime.
Runtime inference, execution, state, and reconciliation belong to the target
deployment path and must be qualified before they can be described as current.

## Does Disuza Quantitative publish current performance?

No. This repository makes no current strategy-performance claim and does not
publish live account performance.

## Can I invest or buy signals?

No. Disuza Quantitative does not accept investment through this repository,
offer a public investment service, or sell trading signals.

## What markets are researched?

**CURRENT:** The core research scope covers BTC and ETH perpetual markets and
NQ and ES index-futures markets. Optional CFD adaptations are evaluated
separately.

Research scope is not a statement of current live trading.

It is programme research scope only, not qualified engine coverage. The narrow
engine contract does not establish coverage of every listed market or the
programme design horizon.

## What is the primary holding horizon?

**CURRENT:** The primary design horizon is approximately 30 minutes to 4 hours.
This is not a high-frequency, co-location-dependent programme.

## Is the signal engine based on machine learning?

**CURRENT:** Primary signal generation is rule-based, not machine-learning
based.

**TARGET:** Machine learning may be researched only in auxiliary roles, such as
meta-labeling, dynamic position sizing, or regime detection, after the related
hard-rule baseline qualifies out of sample.

## What research methodology is used?

**CURRENT:** The current synthetic engine route uses purged, embargoed, anchored
walk-forward evaluation and Deflated Sharpe Ratio (DSR). Combinatorial Purged
Cross-Validation (CPCV) and Probability of Backtest Overfitting (PBO) are
programme methods only where applicable; they are not claimed for the current
synthetic engine route.

These methods reduce overfitting risk; they do not guarantee performance.
See [`research-methodology.md`](research-methodology.md).

## What technology is current?

**CURRENT:** private Python-based research tooling, forward-only market-data
capture and monitoring, data and quality-control work, cloud-supported batch
workflows, and statistical governance.

Specific runtime execution services are not presented as current. The broader
system design is described as a target in [`architecture.md`](architecture.md).

## What engine evidence is current?

**CURRENT:** A bounded execution-engine contract is qualified on deterministic
synthetic fixtures only. It has not processed market data and does not qualify a
strategy, an economic result, paper execution, live execution, or deployment.

## Is the system non-custodial?

Non-custodial operation is a **TARGET** design requirement where applicable.
It is not presented here as a current client relationship or a currently
deployed execution guarantee.

## Is the source code open source?

No. The trading and research source code is proprietary and maintained in
private repositories. This public repository contains a sanitized technical
reference, not the platform source.

## Is Disuza Quantitative a regulated investment service?

No investment service is offered through this repository. Any future service
or deployment model would require separate legal, regulatory, counterparty,
and operational review.

## Can I contribute?

This is a curated public reference. Factual-correction and documentation
clarification issues are welcome. The private trading source is not open for
public contribution.

## How can I make contact?

Email **[contact@disuza.com](mailto:contact@disuza.com)** for general
inquiries.

---

*Disuza Quantitative — Public Technical Reference · Version 4.0.0 candidate ·
Unreleased · Last verified 2026-09-01*
