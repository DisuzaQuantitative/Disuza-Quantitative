# Components

> The public-facing services that make up the Disuza Quantitative platform.
> Internal module structure and implementation details are operational and
> not included.

## Service map

| Service | Tier | Trigger | Purpose |
| --- | --- | --- | --- |
| Data collector | Data plane | Cloud Scheduler (periodic) | Multi-source ingestion, PIT snapshot, schema validation, cache-manifest lineage |
| Signal detector | Compute plane | Pub/Sub event + Cloud Scheduler safety-net | Feature fetch, ensemble ML inference, risk-framework gating, signal publication |
| Hedge monitor | Compute + execution plane | Cloud Scheduler (periodic) | Layered risk overlay, trailing-stop discipline, timeout enforcement, reconciliation sweep |
| Order executor | Execution plane | Pub/Sub event | Venue adapters, order lifecycle, broker-truth reconciliation on exits |
| Retrain job | Compute plane | Cloud Scheduler (monthly) | Periodic model retraining, artefact versioning, active-artefact pointer update |
| Dashboard API | Access layer | HTTPS authenticated | Client portal endpoints for position and analytics reads |
| Public site | Presentation | Static hosting | Guest portal, landing, authenticated client UI |

Each service is independently deployable, independently scaled, and
independently instrumented.

## Data collector

**Purpose.** Periodic multi-source ingestion into the point-in-time
feature pipeline.

**Triggers.** Cloud Scheduler fires on the ingestion cadence. On boot, a
first cycle runs immediately to seed the cache.

**Responsibilities.**

- Fetch from each configured source class (on-chain analytics, exchange
  microstructure, macro context, attention signals).
- Write a point-in-time snapshot of the raw data.
- Validate against the critical-feature schema; fall back to last-known-
  good if validation fails.
- Produce a content-addressed manifest hash and a lineage row in
  BigQuery for long-term audit.
- Publish a cycle-complete event on Pub/Sub.

## Signal detector

**Purpose.** Feature-based position decisions from the ensemble ML engine.

**Triggers.** Primary trigger is the cycle-complete event from the data
collector. A Cloud Scheduler safety-net fires every few hours as a
fallback in case the primary trigger is missed.

**Responsibilities.**

- Resolve the active model artefact from the Firestore pointer.
- Load the per-asset feature vector for the current bar.
- Run ensemble ML inference.
- Apply risk-framework gates (position caps, drawdown gates,
  trading-enabled flag).
- Publish a signal event to the order executor.

## Hedge monitor

**Purpose.** Layered risk overlay, in-flight position discipline, and
reconciliation sweep.

**Triggers.** Cloud Scheduler periodic cadence. Also exposes a manual
reconcile endpoint for operator use.

**Responsibilities.**

- Run the layered risk overlay to modulate exposure when short-horizon
  signals disagree with the primary stance.
- Monitor trailing stops and enforce timeout discipline.
- Before every exit decision, verify the broker still holds the matching
  position (per-exit broker-truth pre-check).
- Run a full reconciliation sweep on boot and on demand: compare
  Firestore state against broker fills, reconstruct orphaned position
  exits from real fill history.

## Order executor

**Purpose.** Venue-specific order placement, monitoring, and close.

**Triggers.** Pub/Sub events from the signal detector and hedge monitor.

**Responsibilities.**

- Route orders to the right venue adapter based on the target account.
- Place orders with stable idempotency keys and client order identifiers.
- Monitor fills and produce structured execution events.
- On close, resolve the real exit price and fees from broker fills,
  reconstruct PnL, and update Firestore state.
- Emit alerts on execution failures or unexpected broker states.

## Retrain job

**Purpose.** Periodic model retraining with artefact versioning.

**Triggers.** Cloud Scheduler monthly cron.

**Responsibilities.**

- Assemble the training window from the PIT feature store.
- Retrain the ensemble ML engine and the layered risk model.
- Write artefacts to Cloud Storage under a versioned path.
- Update the Firestore pointer that the signal detector reads, flipping
  the active artefact with a single atomic write (no redeploy required).
- Emit a retrain-complete event with validation metrics.

## Dashboard API

**Purpose.** Authenticated client portal endpoints.

**Triggers.** HTTPS requests from the public site after authentication.

**Responsibilities.**

- Position reads (open positions, current equity, drawdown state).
- Historical analytics reads (trade ledger, equity curves).
- Configuration reads and limited writes (authorised personnel only).
- System-health summary endpoints.

## Public site

**Purpose.** The public presence at [disuza.com](https://disuza.com). Hosts
the landing page, the guest portal (public demo), LLM context files, and
— after authentication — the operator dashboard.

**Responsibilities.**

- Render marketing and reference content.
- Provide the guest portal with clearly labelled hypothetical-backtest
  simulation data.
- Emit the machine-readable context files at `/llms.txt` and
  `/llms-full.txt`, regenerated from a single source of truth on every
  production build.
- Proxy authenticated requests to the dashboard API.

## Inter-service contracts

- **Event envelope.** Every Pub/Sub event carries: an `idempotency_key`
  (stable across retries), a `source` identifier, a `ts` timestamp, and
  a typed `payload`.
- **Consumer idempotency.** Before acting on an event, consumers check
  a processed-message ledger keyed on `idempotency_key`.
- **State updates.** Firestore writes use optimistic concurrency with
  version counters; conflicts trigger a bounded retry with backoff.
- **Failure propagation.** Unrecoverable errors emit a structured alert
  on Telegram; recoverable errors retry with exponential backoff up to
  a bounded attempt count before alerting.

## What is NOT published

Module-level file layouts, internal APIs, secret-handling patterns,
deploy scripts, runbooks, incident histories, and service-to-service
authentication details are operational and are not part of the public
reference.

---

*Disuza Quantitative — Living Technical Reference · Version 3 · Last Updated: 2026-04-20*

<!-- last_updated: 2026-04-20 · version: 3.0.0 -->
