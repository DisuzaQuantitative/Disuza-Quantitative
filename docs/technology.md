# Technology

> The technology stack at the abstraction level appropriate for public
> reference. Library-level details, container images, and service configuration
> are operational and not included.

## Language and runtime

- **Primary language:** Python 3.12+. Data processing, feature engineering,
  ML inference, execution logic, and service glue.
- **Frontend:** TypeScript 5 with Next.js 16 App Router, React 19, Tailwind
  CSS.
- **Infrastructure-as-code surface:** standard shell tooling plus Google
  Cloud native CLIs.

## Machine learning

- **Engine:** systematic ensemble ML paired with a layered risk model.
- **Tooling:** standard scientific Python and gradient boosting toolchains;
  scikit-learn for general ML utilities.
- **Serving:** containerised on Cloud Run, warm-cached per instance.
- **Training and retraining:** Google Cloud; artefacts persisted to Cloud
  Storage; active artefact selection via a Firestore pointer that can be
  rolled forward without a redeploy.

Specific model architectures, feature counts, and hyperparameters are
proprietary and not published.

## Orchestration and state

Disuza's orchestration is **event-driven**, not DAG-driven:

- **Cloud Scheduler** — the clock. Kicks off ingestion, safety-net
  inference runs, hedge-monitor sweeps, and retraining cycles on cron
  schedules.
- **Pub/Sub** — the event bus. Pipelines communicate by publishing and
  consuming topics. Consumers implement idempotency via a processed-message
  ledger and stable idempotency keys.
- **Firestore** — real-time state. Open positions, account equity,
  kill-switch flags, and configuration pointers live here. Clients read
  near-real-time; writes are transactional where consistency matters.
- **Cloud SQL (PostgreSQL)** — historical analytics. Trade ledger,
  equity curves, per-trade attribution, metrics history.
- **Cloud Storage** — model artefacts, feature snapshots, raw data cache.
- **Artifact Registry** — versioned Docker images for every service.

## Compute

- **Cloud Run services** for every stateless request or event handler:
  data collection, inference, hedging and monitoring, execution,
  dashboard API.
- **Cloud Run jobs** for bounded batch workloads such as monthly
  retraining.
- Auto-scaling with warm-cache-friendly concurrency settings.

## Observability

- **Structured logging** from every service to Cloud Logging.
- **Custom metrics** surfaced via Cloud Monitoring.
- **Heartbeat watchdogs** per service — a missing heartbeat after a
  bounded window alerts operators.
- **Telegram** is the operator alert channel for high-severity events
  (kill-switch trips, orphan detection, deploy outcomes). Email is the
  fallback.

| Concern | Tool |
| --- | --- |
| Log aggregation | Cloud Logging |
| Metrics and dashboards | Cloud Monitoring |
| Error reporting | Cloud Error Reporting |
| Trace (limited) | Cloud Trace |
| Operator alerts | Telegram primary, email fallback |
| Incident memory | Internal runbooks (not public) |

## Security

- Credentials in **Google Cloud Secret Manager**. No credentials in code,
  container images, or repositories.
- Service accounts with **least-privilege IAM** per service.
- **Trade-only credential scoping** on every execution path — no
  service account holds withdrawal or fund-movement permissions.
- **Immutable timestamped audit trail** for every execution decision.
- TLS 1.3 on every request path.

## CI/CD

- **Cloud Build** for container builds and deployments.
- **Artifact Registry** for versioned image storage.
- **Firebase Hosting** for the public website with automatic deploys on
  tagged releases.
- Static type checks and linting on every commit; production-build
  verification on every merge.

## Data providers (class-level)

- On-chain analytics from institutional-tier data providers.
- Exchange OHLC and microstructure from public exchange APIs.
- Macro and attention signals from standard financial and public data
  sources.

Specific vendor names are not published as part of the public reference.

## Frontend

- **Next.js 16** App Router with static export for the public site.
- **React 19** functional components with hooks.
- **Tailwind CSS** for styling.
- **Framer Motion** for interactions.
- **Firebase Hosting** for deployment; CDN-edged globally.

## Development practices

- Type hints across the Python surface; strict TypeScript on the
  frontend.
- Structured commit history with conventional-commit-style prefixes
  (`feat`, `fix`, `chore`, `docs`, `refactor`).
- Single-source-of-truth for published facts via a `facts.ts` export on
  the website side, regenerating `llms.txt` and `llms-full.txt` on every
  production build to prevent drift.
- IP-safety pre-commit grep to prevent leakage of proprietary terms into
  public surfaces.

---

*Disuza Quantitative — Living Technical Reference · Version 3 · Last Updated: 2026-04-20*

<!-- last_updated: 2026-04-20 · version: 3.0.0 -->
