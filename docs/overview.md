# Overview

## Company

Disuza Quantitative is a private quantitative trading research laboratory
headquartered in Madrid, Spain. Founded in 2025 by Yasmine Bendhiab (Co-Founder
& CEO) and Fares Bendhiab (Co-Founder & CTO), Disuza operates as a
closed-access research environment engineering systematic execution algorithms
for digital asset markets.

The firm operates proprietary capital and invitation-only partner accounts. It
is not accepting retail clients, not soliciting retail or professional investor
capital, and not offering regulated investment services at this time.

## Thesis

Human emotion is the largest persistent inefficiency in financial markets.
Disciplined machine learning applied to on-chain and market microstructure
data can extract durable edge — when paired with institutional-grade risk
management and rigorous execution discipline.

Disuza's design stance is that the operational edge compounds from three
sources:

1. **Data quality.** Deterministic point-in-time feature pipelines with
   retroactive-revision guardrails ensure that training and live inference
   see the same world.
2. **Risk discipline.** A layered risk model modulates exposure in response
   to short-horizon regime shifts, rather than betting on a single direction.
3. **Execution fidelity.** Non-custodial execution with broker-truth
   reconciliation — the broker's state is always the source of truth, and
   reconstructed PnL uses actual fills, not algorithmic estimates.

## What Disuza is

- A private **research laboratory** — the primary output is systematic trading
  infrastructure, not a product sold to retail.
- A **closed-access** operator — access to the live platform is by invitation
  only, and participation is limited to proprietary capital plus authorised
  partner accounts.
- A **methodology-transparent** organisation — architecture and posture are
  published in this living reference; source code, model weights, and
  operational know-how remain proprietary.

## What Disuza is NOT

- **Not a high-frequency trading firm.** The firm operates on intraday to
  multi-day horizons, not at microsecond latency.
- **Not a retail-facing product** or signal-selling service. Disuza does not
  offer subscription signals, does not accept retail investment, and does not
  operate as a trading academy.
- **Not a public hedge fund.** The firm is not licensed as a collective
  investment scheme in any jurisdiction and does not hold or manage
  third-party capital as an asset manager.
- **Not a licensed investment firm.** The firm is in a pre-licensing phase
  and monitors the MiCA and FINMA regulatory landscapes. Statements in this
  repository about regulatory alignment are expressions of internal posture,
  not representations of regulatory approval.

## Regulatory posture (summary)

- **Jurisdiction:** Kingdom of Spain, entity registered in Madrid.
- **Phase:** pre-licensing.
- **Framework monitoring:** MiCA (EU) and FINMA (Swiss).
- **Simulated performance disclosure:** CFTC Rule 4.41 acknowledged. All
  performance figures on the public guest portal are hypothetical historical
  simulations.
- **Client relationship model:** non-custodial. Credentials across both
  execution classes are scoped to trade-only operations.
- **Solicitation posture:** closed-access, invitation-only. Disuza does not
  solicit retail or professional investor capital.

Detail in [`regulatory.md`](regulatory.md).

## Technology posture (summary)

- **Engine:** systematic ensemble ML paired with a layered risk model.
- **Data:** multi-source pipeline combining on-chain analytics, exchange
  microstructure, macro context, and attention signals, through point-in-time
  feature pipelines with retroactive-revision guardrails.
- **Execution:** institutional-protocol brokers (FIX-based, trade-only scope)
  and self-custody perpetual venues (trade-scoped API wallets).
- **Cloud:** Google Cloud, event-driven orchestration, non-custodial execution
  with broker-truth reconciliation.

Detail in [`architecture.md`](architecture.md) and [`technology.md`](technology.md).

## Contact

All inquiries — general, partnerships, careers: **[contact@disuza.com](mailto:contact@disuza.com)**.

---

*Disuza Quantitative — Living Technical Reference · Version 3 · Last Updated: 2026-04-20*
*Source of truth: [https://disuza.com/llms-full.txt](https://disuza.com/llms-full.txt)*

<!-- last_updated: 2026-04-20 · version: 3.0.0 -->
