# Regulatory Posture

> Disuza operates in a pre-licensing phase. The statements below describe
> internal posture and monitoring; they do not constitute representations of
> regulatory approval or licensed status.

## Jurisdiction

Disuza Quantitative is a private entity registered in Madrid, Kingdom of
Spain. Operational activity is conducted from that jurisdiction. Documentation
is released under Creative Commons Attribution 4.0 International (see
[`LICENSE`](../LICENSE)), with explicit carve-outs for trademarks, source code,
and operational know-how.

## Phase

The firm operates in a **pre-licensing** phase. It does not hold a
regulated-investment-services licence in any jurisdiction, does not market
investment services to retail clients, and does not solicit retail or
professional investor capital.

## Framework monitoring

Disuza tracks two regulatory landscapes as part of its pre-licensing
preparation:

- **MiCA** — EU Markets in Crypto-Assets Regulation. Relevant provisions
  include the authorisation regime for Crypto-Asset Service Providers
  (CASPs), the conduct-of-business requirements for client-facing
  services, and the prudential requirements for entities that hold
  client assets or execute client orders.
- **FINMA** — Swiss Financial Market Supervisory Authority. Relevant
  guidance includes the CASP-adjacent categorisations under FinIA and
  FinSA, and the cross-border provisioning rules for services offered
  into Switzerland.

These statements reflect internal posture — understanding of the
landscape and preparation for eventual licensing. They do **not**
constitute representations of compliance, authorisation, or approval
by any supervisory authority.

## Counterparty relationships

Disuza's execution counterparties — prop-trading programmes and
self-custody perpetual venues — operate under their own regulatory
umbrellas in their own jurisdictions. Disuza's trading activity through
those counterparties is conducted as the counterparty's authorised trader,
under the counterparty's terms, and does not transfer regulatory
responsibility to Disuza.

## Performance claims and simulated results

Any backtest results referenced on the public guest portal at
[disuza.com/guest](https://disuza.com/guest) are **hypothetical historical
simulations** and do not represent actual trading outcomes. Disuza
acknowledges **CFTC Rule 4.41** regarding simulated performance:

> "HYPOTHETICAL OR SIMULATED PERFORMANCE RESULTS HAVE CERTAIN INHERENT
> LIMITATIONS. UNLIKE AN ACTUAL PERFORMANCE RECORD, SIMULATED RESULTS DO
> NOT REPRESENT ACTUAL TRADING. ALSO, SINCE THE TRADES HAVE NOT ACTUALLY
> BEEN EXECUTED, THE RESULTS MAY HAVE UNDER- OR OVER-COMPENSATED FOR THE
> IMPACT, IF ANY, OF CERTAIN MARKET FACTORS, SUCH AS LACK OF LIQUIDITY.
> SIMULATED TRADING PROGRAMS IN GENERAL ARE ALSO SUBJECT TO THE FACT THAT
> THEY ARE DESIGNED WITH THE BENEFIT OF HINDSIGHT. NO REPRESENTATION IS
> BEING MADE THAT ANY ACCOUNT WILL OR IS LIKELY TO ACHIEVE PROFITS OR
> LOSSES SIMILAR TO THOSE SHOWN."

Public performance figures are framed with a **past performance does not
guarantee future results** disclaimer surfaced at the point of
presentation, not only in a separate modal.

## Backtest methodology (high-level)

At a level appropriate for public reference:

- Out-of-sample validation on held-out windows that the model has not
  seen during training.
- Point-in-time feature snapshots so the backtest sees the same data the
  live engine would have seen at the same historical moment.
- Conservative standard-error estimation for monthly return and
  risk-adjusted-return metrics.
- Deterministic replay: the same raw snapshots reproduce the same
  backtest output end-to-end.

Detailed backtest parameters, validation windows, and metric definitions
are operational and not part of the public reference.

## Custody model

Disuza's relationship with any counterparty is structurally
non-custodial:

- For institutional-protocol prop accounts, the prop firm holds the
  capital and issues Disuza trade-only credentials.
- For self-custody venues, Disuza uses agent wallets under signer
  separation: the online trading key cannot move funds; withdrawal
  requires an offline root signer.

Disuza does not at any time hold, pool, or otherwise have discretionary
access to client funds beyond trade-placement authority.

## Non-solicitation posture

Disuza does not solicit retail investor capital, does not market
investment services to the public in any jurisdiction, and does not
operate as a Collective Investment Scheme under any regulatory framework.
Access to Disuza's live platform is closed and by invitation only.

## Document status

This documentation is informational only. Statements about regulatory
alignment describe internal posture and monitoring activity; they do not
constitute representations of regulatory compliance, authorisation, or
approval. Before engaging with Disuza Quantitative in any capacity,
consult local counsel.

---

*Disuza Quantitative — Living Technical Reference · Version 3 · Last Updated: 2026-04-20*

<!-- last_updated: 2026-04-20 · version: 3.0.0 -->
