# System Architecture

> This document provides an overview of the Disuza Quantitative trading platform architecture. Implementation details and proprietary algorithms are omitted.

## Design Philosophy

The platform is built on several core principles:

1. **Pipeline-Driven Architecture**: All workflows orchestrated through Apache Airflow DAGs for reliability and observability.
2. **Domain-Driven Design**: Clear separation between data ingestion, feature engineering, model inference, and execution domains.
3. **Fail-Safe Operations**: Every component is designed to fail gracefully with automatic recovery and state persistence.
4. **Observability First**: Comprehensive logging, metrics, and tracing built into every service from day one.

---

## High-Level Architecture

```
                                    ┌──────────────────────────────────────┐
                                    │          CONTROL PLANE               │
                                    │  ┌────────────────────────────────┐  │
                                    │  │      Operations Dashboard      │  │
                                    │  │      (Next.js + FastAPI)       │  │
                                    │  └────────────────────────────────┘  │
                                    └───────────────────┬──────────────────┘
                                                        │
        ┌───────────────────────────────────────────────┼───────────────────────────────────────────────┐
        │                                               │                                               │
        ▼                                               ▼                                               ▼
┌───────────────────┐                       ┌───────────────────┐                       ┌───────────────────┐
│    DATA PLANE     │                       │   COMPUTE PLANE   │                       │  EXECUTION PLANE  │
│                   │                       │                   │                       │                   │
│ ┌───────────────┐ │                       │ ┌───────────────┐ │                       │ ┌───────────────┐ │
│ │  Market Data  │ │       ────────▶       │ │  ML Pipeline  │ │       ────────▶       │ │ Risk Manager  │ │
│ │   Ingestion   │ │                       │ │  (Inference)  │ │                       │ │               │ │
│ └───────────────┘ │                       │ └───────────────┘ │                       │ └───────────────┘ │
│                   │                       │                   │                       │                   │
│ ┌───────────────┐ │                       │ ┌───────────────┐ │                       │ ┌───────────────┐ │
│ │   On-Chain    │ │                       │ │    Feature    │ │                       │ │  Order Router │ │
│ │   Analytics   │ │                       │ │    Engine     │ │                       │ │               │ │
│ └───────────────┘ │                       │ └───────────────┘ │                       │ └───────────────┘ │
│                   │                       │                   │                       │                   │
│ ┌───────────────┐ │                       │ ┌───────────────┐ │                       │ ┌───────────────┐ │
│ │  Macro Regime │ │                       │ │    Signal     │ │                       │ │   Position    │ │
│ │  Classifier   │ │                       │ │   Generator   │ │                       │ │    Manager    │ │
│ └───────────────┘ │                       │ └───────────────┘ │                       │ └───────────────┘ │
│                   │                       │                   │                       │                   │
└───────────────────┘                       └───────────────────┘                       └───────────────────┘
        │                                               │                                        │
        └───────────────────────────────────────────────┼────────────────────────────────────────┘
                                                        │
                                    ┌───────────────────▼──────────────────┐
                                    │       ORCHESTRATION LAYER            │
                                    │                                      │
                                    │   Apache Airflow (Cloud Composer)    │
                                    │   DAGs │ Scheduling │ Monitoring     │
                                    │                                      │
                                    └───────────────────┬──────────────────┘
                                                        │
                                    ┌───────────────────▼──────────────────┐
                                    │        PERSISTENCE LAYER             │
                                    │                                      │
                                    │  Cloud SQL │ Redis │ Cloud Storage   │
                                    │                                      │
                                    └──────────────────────────────────────┘
```

---

## Component Details

### Data Plane

The data plane is responsible for ingesting, normalizing, and distributing market data from multiple sources.

#### Market Data Ingestion

- **Protocol**: REST APIs for scheduled data pulls
- **Sources**: Major cryptocurrency exchanges
- **Processing**: Normalization, deduplication, gap detection
- **Output**: Unified market data format stored in Cloud SQL

#### On-Chain Analytics

- **Sources**: Blockchain analytics providers (Glassnode)
- **Metrics**: Network activity, whale movements, exchange flows
- **Frequency**: Configurable polling intervals via Airflow
- **Integration**: Enriches market data with on-chain context

#### Macro Regime Classifier

- **Inputs**: Cross-market indicators, volatility indices
- **Output**: Current market regime classification
- **Purpose**: Contextualizes trading decisions based on macro environment

### Compute Plane

The compute plane handles all feature engineering and model inference.

#### Feature Engine

- **Architecture**: Batch feature computation via scheduled DAGs
- **Categories**: Technical, on-chain, macro, derivatives
- **Storage**: Feature store with point-in-time correctness
- **Versioning**: Feature definitions tracked and versioned

#### ML Pipeline

- **Framework**: LightGBM-based ensemble models
- **Architecture**: Hierarchical gating with specialized experts
- **Serving**: Cloud Run inference with configurable batch sizes
- **Monitoring**: Prediction distribution tracking, drift detection

#### Signal Generator

- **Logic**: Combines model outputs with rule-based filters
- **Output**: Structured trading signals with metadata
- **Routing**: Signals published to execution plane via Pub/Sub

### Execution Plane

The execution plane handles all order management and risk controls.

#### Risk Manager

- **Pre-Trade**: Position limits, exposure checks, drawdown gates
- **Real-Time**: P&L monitoring, margin utilization
- **Post-Trade**: Fill analysis, slippage tracking

#### Order Router

- **Venues**: Multi-exchange support (CEX, DEX, OTC)
- **Protocols**: REST APIs for order submission
- **Smart Routing**: Venue selection based on liquidity and costs

#### Position Manager

- **Tracking**: Position reconciliation
- **Lifecycle**: Entry, scaling, exit management
- **Reporting**: P&L attribution, trade history

---

## Communication Patterns

### Synchronous (Request-Response)

- Dashboard API calls
- Configuration updates
- Health checks

### Asynchronous (Pub/Sub)

- Signal propagation between pipeline stages
- Trade notifications
- Alert distribution

### Scheduled (Airflow DAGs)

- Data ingestion pipelines
- Feature computation
- Model inference batches

---

## Deployment Architecture

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         Google Cloud Platform                           │
│                                                                         │
│  ┌───────────────────────────────────────────────────────────────────┐  │
│  │                      Cloud Composer (Airflow)                     │  │
│  │                                                                   │  │
│  │   ┌─────────────┐  ┌─────────────┐  ┌─────────────┐               │  │
│  │   │  Data DAGs  │  │   ML DAGs   │  │  Exec DAGs  │               │  │
│  │   └─────────────┘  └─────────────┘  └─────────────┘               │  │
│  │                                                                   │  │
│  └───────────────────────────────────────────────────────────────────┘  │
│                                 │                                       │
│                                 ▼                                       │
│  ┌───────────────────────────────────────────────────────────────────┐  │
│  │                       Cloud Run Services                          │  │
│  │                                                                   │  │
│  │   ┌───────────┐  ┌───────────┐  ┌───────────┐  ┌───────────┐      │  │
│  │   │   Data    │  │    ML     │  │ Execution │  │ Dashboard │      │  │
│  │   │  Pipeline │  │ Inference │  │  Engine   │  │    API    │      │  │
│  │   └───────────┘  └───────────┘  └───────────┘  └───────────┘      │  │
│  │                                                                   │  │
│  └───────────────────────────────────────────────────────────────────┘  │
│                                 │                                       │
│                                 ▼                                       │
│  ┌───────────────────────────────────────────────────────────────────┐  │
│  │                       Managed Services                            │  │
│  │                                                                   │  │
│  │   ┌───────────┐  ┌───────────┐  ┌───────────┐  ┌───────────┐      │  │
│  │   │ Cloud SQL │  │ Memorystr │  │  Pub/Sub  │  │  Secret   │      │  │
│  │   │ Postgres  │  │  (Redis)  │  │           │  │  Manager  │      │  │
│  │   └───────────┘  └───────────┘  └───────────┘  └───────────┘      │  │
│  │                                                                   │  │
│  └───────────────────────────────────────────────────────────────────┘  │
│                                                                         │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Scalability Considerations


| Component      | Scaling Strategy                        |
| -------------- | --------------------------------------- |
| Data Ingestion | Horizontal (partition by symbol)        |
| Feature Engine | Horizontal (stateless computation)      |
| ML Inference   | Horizontal with load balancing          |
| Execution      | Vertical (single coordinator per venue) |
| Database       | Read replicas, connection pooling       |

---

## Resilience

### Error Handling


| Scenario                | Response                            |
| ----------------------- | ----------------------------------- |
| Data source unavailable | Retry with backoff, use cached data |
| Execution venue down    | Route to alternate venue            |
| Airflow task failure    | Retry policy, Telegram alerting     |

### State Management

- **SQL Persistence**: Trade state and positions stored in Cloud SQL
- **Firestore**: Execution engine state management
- **Redis**: Hot data caching for performance

---

## Security Architecture

### Authentication & Authorization

- Service accounts with minimal permissions
- API keys managed via Secret Manager
- JWT authentication for dashboard access

### Data Protection

- Encryption at rest and in transit
- Secrets in Secret Manager (never in code)
- Firestore for secure state management

---

*For more details on specific components, see the respective documentation in this folder.*
