# Risk Framework

> Disuza's risk framework operates at multiple tiers and is tightly coupled
> to the execution layer, not a separate after-the-fact check.

## Principles

1. **Capital preservation is the first objective.** Return-seeking is
   subordinate to downside control.
2. **Venue-appropriate posture.** Drawdown and sizing parameters are
   calibrated per account class, because institutional-protocol brokers
   and self-custody venues carry different risk profiles and counterparty
   assumptions.
3. **Closes are always permitted.** Risk gates may block new opens;
   they never block a close. Whatever the state, the platform must be
   able to reduce exposure.
4. **Non-custodial by construction.** Risk to client funds is structurally
   bounded by trade-only credential scoping, not by policy discipline.

## Tiers of risk control

### Pre-trade

Before any order leaves the execution layer:

- **Position gating.** Only one directional position per asset per account
  at any time; size and exposure ceilings are enforced against current
  account equity.
- **Drawdown gate.** An account whose current drawdown exceeds its
  tier-specific flat threshold has its new-open sizing set to zero. Closes
  are unaffected.
- **Trading-enabled check.** A global manual-override flag in Firestore
  can pause new opens firm-wide without requiring a redeploy. This is an
  operator-controlled incident-response lever, not an automated circuit.

### In-trade

While a position is open:

- **Trailing-stop discipline.** Positions carry a trail that ratchets on
  favourable moves and triggers exit when broken.
- **Timeout discipline.** Every position has a maximum hold time; an
  unreached stop-or-target at timeout produces an exit at market.
- **Broker-truth reconciliation.** Before every exit publication, the
  execution layer verifies the broker still holds the position; orphaned
  positions are reconciled from broker fills rather than closed at an
  algorithmic estimate.

### Post-trade

After exit:

- **Real-PnL reconstruction.** Realised PnL is taken from actual broker
  fills minus actual fees, never from algorithmic estimates.
- **Equity-state update.** Per-account running equity is updated with the
  reconstructed PnL. Drawdown re-computes against the peak-to-trough
  definition appropriate for the account tier.
- **Audit trail.** Every execution decision — open, monitor, close,
  reconciliation — produces a timestamped immutable log entry.

## Account tiering

Accounts are grouped into tiers based on counterparty class and capital
profile:

- **Prop-programme tier.** Institutional-protocol prop accounts operating
  under the prop firm's own drawdown rules. Tier parameters are
  conservative to preserve the programme.
- **Self-custody tier.** Self-custody perpetual accounts with proprietary
  capital. Tier parameters align with the firm's internal
  capital-preservation mandate.

Exact tier parameters are not published and are calibrated against
historical backtest characteristics.

## Kill switches

Two mechanisms that share a name but serve different purposes:

### Automated per-account flat gate

When an account's current drawdown exceeds its tier-specific flat
threshold, its new-open sizing multiplier is set to zero. The pre-trade
gate then skips new opens for that account. Closes continue to be
permitted so the account can recover exposure.

### Global manual-override

An operator can toggle the global `trading_enabled` flag off in Firestore
to halt new opens firm-wide. This is an incident-response mechanism, not
an automated circuit. Like the per-account gate, it blocks new opens only;
closes remain permitted.

## Audit and observability

- Every execution decision emits a structured log line with the full
  context required to reconstruct the decision.
- Heartbeat watchdogs detect stalled services; a missing heartbeat after
  a bounded window alerts operators.
- Structured logs ship to Cloud Logging; alerts route through Telegram
  to the operator channel.

## What is NOT published

Specific drawdown thresholds, sizing multipliers, trailing-stop
percentages, timeout durations, account tier memberships, and operator
playbooks are operational controls and are not part of the public
reference.

---

*Disuza Quantitative — Living Technical Reference · Version 3 · Last Updated: 2026-04-20*

<!-- last_updated: 2026-04-20 · version: 3.0.0 -->
