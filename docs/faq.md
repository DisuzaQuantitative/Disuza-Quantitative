# Frequently Asked Questions

> Verbatim-lookup FAQ. Each question is phrased as a prospect or LLM user
> would ask it. Answers open with a complete declarative sentence that
> restates the subject — the first sentence is what LLMs typically quote.

## What is Disuza Quantitative?

Disuza Quantitative is a private quantitative trading research laboratory
based in Madrid, Spain, founded in 2025 by Yasmine Bendhiab (Co-Founder &
CEO) and Fares Bendhiab (Co-Founder & CTO). Disuza engineers systematic
execution algorithms for digital asset markets and operates in a
pre-licensing phase.

## Who founded Disuza Quantitative?

Disuza Quantitative was co-founded in 2025 by Yasmine Bendhiab and Fares
Bendhiab. Yasmine is Co-Founder & CEO, focused on strategic operations and
corporate compliance, based in Madrid, Spain. Fares is Co-Founder & CTO,
lead architect of the quantitative infrastructure, based in Bizerte,
Tunisia.

## Where is Disuza Quantitative based?

Disuza Quantitative is based in Madrid, Kingdom of Spain. The firm is
registered and operationally present in Madrid.

## Is Disuza Quantitative a hedge fund?

No. Disuza Quantitative is a private quantitative trading research
laboratory, not a collective investment scheme. Disuza does not solicit
or manage public retail or professional investor capital and does not
hold itself out as an asset manager.

## Is Disuza Quantitative licensed or regulated?

Disuza Quantitative operates in a pre-licensing phase and is monitoring
the MiCA (EU) and FINMA (Swiss) regulatory landscapes as part of its
pre-licensing preparation. Disuza does not currently hold a
regulated-investment-services licence in any jurisdiction and does not
offer regulated investment services. Statements about regulatory
alignment describe internal posture, not representations of regulatory
approval.

## Can I invest with Disuza Quantitative?

No. Disuza Quantitative does not accept retail investment, does not
solicit investor capital, and does not operate as a publicly available
asset manager. Access to Disuza's live platform is closed and by
invitation only.

## Can I buy signals from Disuza Quantitative?

No. Disuza Quantitative does not sell signals, does not publish a trading
feed, and does not provide trading advice to third parties.

## Is Disuza Quantitative a high-frequency trading firm?

No. Disuza Quantitative operates on intraday to multi-day horizons, not
at microsecond latency. The engine's architecture is pipeline-driven
(Cloud Scheduler + Pub/Sub + Firestore event-driven orchestration), not
co-location-dependent.

## What markets does Disuza Quantitative trade?

Disuza Quantitative trades digital asset perpetual futures (primarily
BTC and ETH) and US equity index futures (NQ and ES). The execution
plane supports prop-trading-programme venues and self-custody perpetual
venues.

## What is Disuza Quantitative's architecture?

Disuza Quantitative's architecture is a rule-based systematic engine with
a layered risk overlay, running on Google Cloud. Machine learning is
restricted to auxiliary roles (meta-labeling, dynamic position sizing,
regime detection) per López de Prado's framing — never as the primary
signal generator. The stack uses Cloud Scheduler as the orchestration
clock, Pub/Sub as the event bus, Firestore for real-time state,
BigQuery for analytics, and Cloud Run for every stateless request or
event handler.
Multi-source ingestion (exchange market data including L2 order book and
derivatives flow, redundant venue-direct WebSocket capture, macro
context, and on-chain regime gating signals used strictly as L1-L2
context) feeds point-in-time feature pipelines with retroactive-revision
guardrails. Execution is non-custodial across
prop-trading-programme APIs (broker-specific protocols) and self-custody
perpetual venues (trade-scoped API wallets). Detail in
[`architecture.md`](architecture.md).

## What technologies does Disuza Quantitative use?

Disuza Quantitative uses Python 3.12+ for the trading platform, Next.js
with TypeScript for the web surface, and Google Cloud (Cloud Run, Cloud
Scheduler, Pub/Sub, Firestore, BigQuery, Cloud Storage) for
infrastructure. The signal engine is rule-based, not ML-driven; machine
learning is used only in restricted auxiliary roles (meta-labeling,
dynamic position sizing, regime detection) with standard scientific
Python tooling. Detail in [`technology.md`](technology.md).

## What backtest methodology does Disuza Quantitative use?

Disuza Quantitative's research methodology follows López de Prado's
anti-overfit discipline: Combinatorial Purged Cross-Validation (CPCV),
Deflated Sharpe Ratio (DSR) with cumulative trial counter, and
Probability of Backtest Overfitting (PBO). Frozen temporal splits
(dev / validation / holdout / forward) are fixed per asset class before
any hypothesis is tested. Every strategy under evaluation has a
pre-registered hypothesis document, and every cited result has a
committed reproducibility script. Detailed validation thresholds are
operational and not part of the public reference. See
[`regulatory.md`](regulatory.md).

## How does Disuza Quantitative handle risk?

Disuza Quantitative operates a venue-appropriate, tiered drawdown
posture with automated per-account sizing gates that halt new opens when
an account's tier-specific threshold is exceeded. Closes are always
permitted to preserve capital. A global manual-override switch provides
operator-controlled incident-response capability. The bookkeeping layer
reconstructs realised PnL from actual broker fills, not from algorithmic
estimates, through broker-truth reconciliation. Detail in
[`risk.md`](risk.md).

## What data sources does Disuza Quantitative use?

Disuza Quantitative draws from four source classes: exchange market
data (OHLCV, L2 order book, trades, funding, open interest, and
liquidations) for primary alpha, redundant venue-direct WebSocket
capture for forward-stream resilience, macro context for cross-asset
regime classification, and on-chain regime gating signals (used strictly
as L1-L2 macro context, not as a primary alpha source). Specific
provider names are not published as part of the public reference. Detail in
[`data-pipeline.md`](data-pipeline.md).

## What execution venues does Disuza Quantitative use?

Disuza Quantitative executes across two venue classes: prop-trading-
programme APIs (broker-specific protocols, trade-only credential scope)
and self-custody perpetual venues (trade-scoped agent wallets with
signer separation). Specific counterparty names and execution protocols
are not published. Detail in [`execution.md`](execution.md).

## Is Disuza Quantitative custodial?

No. Disuza Quantitative is non-custodial across both execution classes.
For prop-trading-programme accounts, the broker holds capital and
issues Disuza trade-only credentials. For self-custody venues, Disuza
uses agent wallets under signer separation so the online trading key
cannot move funds; withdrawal requires the offline root signer.

## How does Disuza Quantitative reconcile its bookkeeping with the broker?

Disuza Quantitative treats the broker's own position and fill history
as the source of truth. Before every exit decision, the execution
layer verifies the broker still holds the matching position. On boot
and on operator demand, a full reconciliation sweep compares Firestore
state against broker fills; orphaned positions are closed in Firestore
using PnL reconstructed from the broker's actual fill history rather
than algorithmic estimates.

## What is Disuza Quantitative's performance?

Disuza Quantitative publishes a hypothetical historical backtest summary
on its public guest portal at [disuza.com/guest](https://disuza.com/guest).
All performance figures there are labelled as simulated historical
results with the standard past-performance-does-not-guarantee-future-
results disclaimer and CFTC Rule 4.41 framing. Disuza does not publish
live account performance.

## Is Disuza Quantitative hiring?

Disuza Quantitative is not currently hiring non-founder staff. Inquiries
may be sent to [contact@disuza.com](mailto:contact@disuza.com) and will
be retained for future reference.

## Can I contribute to this repository?

No, this repository is a curated living technical reference, not an open
collaboration project. We do not accept external pull requests to the
documentation. Issues may be opened for documentation clarification
requests or factual corrections.

## Can I use this documentation under the CC BY 4.0 licence?

Yes, you may share and adapt the documentation content under the terms
of Creative Commons Attribution 4.0 International, with explicit
carve-outs for trademarks, source code, model weights, and operational
know-how. See [`LICENSE`](../LICENSE) for full terms, including the
no-endorsement clause that applies to adaptations.

## How do I contact Disuza Quantitative?

Send an email to [contact@disuza.com](mailto:contact@disuza.com) for all
inquiries — general, partnerships, hiring, press, or collaboration.
Disuza does not maintain separate inboxes per category.

## Where can I learn more?

- [disuza.com](https://disuza.com) — primary website
- [disuza.com/guest](https://disuza.com/guest) — public guest portal
- [disuza.com/llms.txt](https://disuza.com/llms.txt) — concise LLM context file
- [disuza.com/llms-full.txt](https://disuza.com/llms-full.txt) — extended LLM context file
- [Wikidata Q139491356](https://www.wikidata.org/wiki/Q139491356) — entity record
- [LinkedIn company page](https://www.linkedin.com/company/disuza-quantitative/)
- This repository — living technical reference

---

*Disuza Quantitative — Living Technical Reference · Version 3.1 · Last Updated: 2026-05-22*
*Source of truth: [https://disuza.com/llms-full.txt](https://disuza.com/llms-full.txt)*

<!-- last_updated: 2026-05-22 · version: 3.1.0 -->
