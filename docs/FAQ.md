# Frequently Asked Questions

## General

### What is Disuza Quantitative?

Disuza Quantitative is an algorithmic trading platform that uses machine learning to generate and execute trading signals in cryptocurrency markets. The platform processes market data, on-chain analytics, and macro indicators through Apache Airflow orchestrated pipelines to make autonomous trading decisions.

### Is this a production system?

Yes. The architecture and technologies described here are from a live trading system. However, all proprietary logic, trading strategies, and alpha-generating code are kept in private repositories.

### Why is this repository public?

This repository serves as a portfolio showcase to demonstrate technical capabilities and system design skills. It's intended for potential employers, collaborators, and the broader tech community to evaluate our engineering practices.

---

## Technical

### What technologies are used?

The platform is built with:
- **Backend**: Python 3.12+, FastAPI, asyncio
- **ML**: LightGBM, Pandas, NumPy, Scikit-learn
- **Frontend**: Next.js 14, React 18, TypeScript, TailwindCSS
- **Orchestration**: Apache Airflow (Cloud Composer)
- **Infrastructure**: Google Cloud Platform (Cloud Run, Cloud SQL, Pub/Sub, etc.)
- **DevOps**: Docker, Cloud Build

### Why Python for trading?

Python offers:
1. Rich ecosystem for data science and ML
2. Excellent async support for concurrent operations
3. Fast development iteration
4. Easy integration with various APIs
5. Strong typing support with type hints

For compute-intensive operations, we use optimizations like NumPy vectorization.

### Why GCP over AWS/Azure?

GCP was chosen for:
- Excellent managed services (Cloud Run, Cloud Composer)
- Competitive pricing for our workload profile
- Cloud Composer provides managed Apache Airflow
- Good integration with ML tools (Vertex AI)
- Team familiarity

The architecture is largely cloud-agnostic and could be migrated if needed.

### How do you handle data ingestion?

We use REST API connections to exchange and data provider endpoints:
- Scheduled data pulls via Airflow DAGs
- API rate limit management
- Schema validation and normalization
- Storage to Cloud SQL for downstream processing

### How do you ensure ML model quality?

Our model validation includes:
- Walk-forward cross-validation
- Out-of-sample testing on held-out periods
- Regime-aware performance analysis
- Production monitoring for prediction drift
- Automated retraining pipelines via Airflow

---

## Architecture

### Why use Apache Airflow?

Airflow (via Cloud Composer) provides:
1. Visual DAG management and monitoring
2. Retry policies and failure handling
3. Scheduling with complex dependencies
4. Built-in logging and alerting
5. Scalable task execution

### Why microservices?

The trading platform benefits from microservices because:
1. Independent scaling of components (execution needs different resources than ML)
2. Fault isolation (ML crash doesn't affect execution)
3. Technology flexibility (can use different tools per service)
4. Team independence (parallel development)

### How do services communicate?

- **Synchronous**: REST APIs for request-response patterns
- **Asynchronous**: Pub/Sub for event distribution
- **Scheduled**: Airflow DAGs for pipeline orchestration

### How do you handle failures?

Every component is designed with failure in mind:
- Health checks and auto-restart
- Circuit breakers for downstream dependencies
- Retry logic with exponential backoff
- State persistence for recovery
- Airflow retry policies for failed tasks

### Is the system high-frequency trading (HFT)?

No. We operate on a pipeline-based architecture with scheduled data processing. Our trading decisions operate on minute-to-hour timeframes. The system is designed for reliability and accuracy rather than microsecond latency.

---

## Execution

### What exchanges/venues are supported?

The execution engine supports:
- **MetaTrader 5** (via broker connections)
- **Binance** (spot and futures)
- **Hyperliquid** (perpetuals)

The architecture allows adding new venues through a standardized interface.

### How are risks managed?

Risk management operates at multiple levels:
1. **Pre-trade**: Position limits, exposure checks
2. **Active**: Drawdown monitoring, P&L alerts
3. **Post-trade**: Fill analysis, slippage tracking
4. **System-level**: Kill switches, circuit breakers

### How do you handle API rate limits?

- Request queuing with rate limiting
- Exponential backoff on 429 responses
- Distributed rate limit tracking in Redis
- Batch operations where possible
- Scheduled pulls to respect provider limits

---

## Security

### How are secrets managed?

All secrets are stored in GCP Secret Manager:
- Never committed to code
- Accessed at runtime via service account
- Rotated regularly
- Audited access

### How is data protected?

- Encryption at rest (AES-256)
- Encryption in transit (TLS 1.3)
- Service account isolation
- IAM for access control
- Audit logging enabled

---

## Operations

### How is the system monitored?

We use GCP's native observability stack:
- **Cloud Logging**: Structured logs from all services
- **Cloud Monitoring**: Custom metrics and dashboards
- **Alerts**: Telegram integration for notifications
- **Airflow UI**: DAG monitoring and task status
- **Alerts**: Telegram integration

### What's the deployment process?

1. Code push triggers Cloud Build
2. Tests run in CI
3. Docker image built and pushed
4. Staged deployment to test environment
5. Integration tests
6. Production deployment with canary
7. Health verification
8. Full traffic migration

### How often do you deploy?

We follow continuous deployment principles:
- Multiple deploys per day for non-critical changes
- Careful rollout for trading logic changes
- Feature flags for gradual rollout
- Instant rollback capability

---

## Career/Collaboration

### Are you hiring?

For current opportunities, please email: careers@disuza.com

### Can I contribute to this repository?

This is a read-only portfolio repository. We're not accepting contributions, but we're happy to discuss technical topics in issues.

### Can I use this code/architecture for my own project?

This repository is licensed under Apache 2.0. You may use the publicly shared documentation and concepts according to the license terms. Note that all proprietary trading logic remains private and is not included here.

---

*Have more questions? Open an issue or email contact@disuza.com*
