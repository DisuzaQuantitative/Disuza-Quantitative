# Operations

> Deployment, monitoring, and reliability posture at the abstraction level
> appropriate for public reference. Operational cadences, alert thresholds,
> and runbook contents are internal and not included.

## Deployment

Services deploy independently through Cloud Build. The public website is
hosted on Firebase Hosting with automatic deploys on tagged releases.
Backend services deploy to Cloud Run from Artifact Registry with
version-tagged images.

Rollbacks are near-instantaneous: Cloud Run retains previous revisions,
and the Firestore active-artefact pointer can be flipped back to the
prior model version with a single write. Firebase Hosting retains
historical releases with a one-command rollback.

## Monitoring

The observability posture combines:

- **Structured logs** from every service to Cloud Logging, queryable via
  the Log Explorer.
- **Custom metrics** for per-service health (request rates, error
  rates, latency distributions) and platform health (positions by
  state, equity, drawdown).
- **Heartbeat watchdogs** — each service emits a periodic heartbeat.
  Missing heartbeats beyond a bounded window alert operators.
- **Telegram** as the primary operator alert channel; email as
  fallback for cold incidents.

## Alerting posture

The alert taxonomy distinguishes operational severity from business
impact:

- **Critical:** trading-continuity issues (broker connectivity, kill
  switch trips, unexpected broker state). Always page.
- **Warning:** recoverable degradation (source unavailable with LKG
  fallback active, schema drift flagged). Notify without paging.
- **Info:** routine state transitions (deploys, retrain cycles,
  reconciliation results). Log only.

Alert thresholds, pager routing, and runbook-association are
operational details and not published.

## Reliability posture

- **Fault tolerance.** Exponential-backoff retries on transient
  failures. Last-known-good fallbacks on data-source outages.
- **At-least-once delivery.** Pub/Sub guarantees at-least-once; consumers
  produce exactly-once effects via a processed-message ledger keyed on
  stable idempotency identifiers.
- **State recovery.** Services are stateless from a request perspective;
  persistent state lives in Firestore and Cloud SQL. A service can restart
  at any time and resume operation.
- **Broker-truth reconciliation.** The platform's bookkeeping is always
  a reconstruction of the broker's ledger, not an authoritative record.
  Drift is detected and corrected on every exit decision and in boot
  sweeps.

## Deployment practices

- **Staged rollout** for code changes: tests in CI, build, staging verification,
  then production.
- **Feature-flagged changes** for behavioural changes: a config flag in
  Firestore can gate a new behaviour without requiring a redeploy.
- **Immutable artefacts.** Container images are tagged by commit SHA and
  never overwritten.
- **Zero-downtime deploys** for request-handling services; model-artefact
  rollovers happen atomically via the active-artefact pointer.

## Change management

Model-behaviour changes follow a more cautious process than code
changes:

1. Train the candidate artefact offline.
2. Validate on a held-out backtest window.
3. Shadow-run against live data for a bounded period (predictions
   logged without being acted upon).
4. Compare shadow predictions against live signals.
5. Flip the active-artefact pointer on operator approval.
6. Monitor live performance against the shadow baseline for a settling
   period.

Specific validation thresholds, shadow-run durations, and approval
criteria are operational and not part of the public reference.

## Incident response

Incidents are categorised by trading-continuity impact:

- **P0 — trading halted.** The global `trading_enabled` flag is toggled
  off; investigation begins immediately; scheduled communication to
  affected account holders.
- **P1 — degraded execution.** Affected account or venue is
  quarantined; trading continues elsewhere; investigation begins
  immediately.
- **P2 — observability or reporting issue.** Fixed in the next
  business-hours cycle.

Runbooks, response-time commitments, and communication templates are
internal and not part of the public reference.

## What is NOT published

Specific operational cadences (ingestion rate, reconciliation frequency,
watchdog timeouts), alert thresholds, runbook contents, on-call rotation
details, incident histories, and internal tooling are not part of the
public reference.

---

*Disuza Quantitative — Living Technical Reference · Version 3 · Last Updated: 2026-04-20*

<!-- last_updated: 2026-04-20 · version: 3.0.0 -->
