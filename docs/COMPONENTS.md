# Component Overview

> High-level descriptions of the major system components.

---

## 1. Core Trading Platform (`src/`)

The heart of the system, handling data processing, feature engineering, and ML inference.

### Subcomponents

| Directory       | Purpose                      | Key Technologies               |
|-----------------|------------------------------|--------------------------------|
| `core/`         | Shared infrastructure        | Pub/Sub, Redis, State Mgmt     |
| `data_pipeline/`| Data ingestion & processing  | REST APIs, Pandas              |
| `features/`     | Feature engineering engine   | NumPy, Custom DSL              |
| `ML/`           | Model training & inference   | LightGBM, Scikit-learn         |
| `ml_pipelines/` | Pipeline orchestration       | Custom framework               |
| `functions/`    | Cloud Run deployments        | FastAPI, Docker                |
| `utils/`        | Shared utilities             | Logging, Config, I/O           |

### Key Capabilities

- **Scheduled data processing** via Airflow DAGs
- **Feature computation** across multiple data domains
- **Model inference** with hierarchical gating
- **Horizontal scalability** through stateless design

---

## 2. Execution Engine (`trading-execution-engine/`)

A separate, highly-optimized service for order execution and position management.

### Architecture

```
┌──────────────────────────────────────────────────────────────────┐
│                        Execution Engine                          │
│                                                                  │
│  ┌──────────────┐    ┌──────────────┐    ┌──────────────┐        │
│  │  Dispatcher  │───▶│   Workers    │───▶│   Executors  │        │
│  │              │    │              │    │              │        │
│  │  • Signal    │    │  • MT5       │    │  • MT5       │        │
│  │    routing   │    │  • Binance   │    │  • Binance   │        │
│  │  • Priority  │    │  • Hyperliquid    │  • Hyperliquid        │
│  │    queue     │    │              │    │              │        │
│  └──────────────┘    └──────────────┘    └──────────────┘        │
│           │                  │                   │                │
│           └──────────────────┼───────────────────┘                │
│                              ▼                                    │
│                    ┌──────────────┐                               │
│                    │ Risk Manager │                               │
│                    │              │                               │
│                    │ • Position   │                               │
│                    │   limits     │                               │
│                    │ • Drawdown   │                               │
│                    │   controls   │                               │
│                    │ • Exposure   │                               │
│                    │   checks     │                               │
│                    └──────────────┘                               │
│                                                                  │
└──────────────────────────────────────────────────────────────────┘
```

### Subcomponents

| Directory           | Purpose                              |
|---------------------|--------------------------------------|
| `src/core/`         | Configuration, models, base classes  |
| `src/dispatcher/`   | Signal routing and prioritization    |
| `src/execution/`    | Venue-specific execution logic       |
| `src/workers/`      | Background processing workers        |
| `external-watchdog/`| Health monitoring service            |

### Features

- **Multi-venue support**: MT5, Binance, Hyperliquid
- **Risk controls**: Pre-trade validation, position limits
- **Notifications**: Telegram integration for trade alerts
- **Resilience**: Automatic reconnection, state recovery

---

## 3. Dashboard Backend (`disuza-dashboard-backend/`)

RESTful API serving the operations dashboard.

### Technology Stack

- **Framework**: FastAPI (Python)
- **Database**: PostgreSQL (Cloud SQL)
- **Cache**: Redis (Memorystore)
- **Auth**: JWT-based authentication

### API Categories

| Router                  | Endpoints                      |
|-------------------------|--------------------------------|
| `auth.py`               | Login, logout, token refresh   |
| `dashboard.py`          | Positions, trades, P&L         |
| `dashboard_snippets.py` | Widget data, summaries         |

### Key Features

- Position data retrieval
- Historical trade analytics
- System health metrics
- Configuration management

---

## 4. Dashboard Frontend (`disuza-site/`)

Modern web application for monitoring and operations.

### Technology Stack

- **Framework**: Next.js 14 (App Router)
- **UI**: React 18, TailwindCSS
- **Deployment**: Vercel (Edge)

### Page Structure

| Route                  | Purpose                |
|------------------------|------------------------|
| `/`                    | Landing page           |
| `/dashboard`           | Overview               |
| `/dashboard/analytics` | Performance analytics  |
| `/dashboard/execution` | Trade execution view   |
| `/dashboard/logs`      | System logs            |
| `/dashboard/settings`  | Configuration          |

### UI Components

- `Hero.tsx` - Landing page hero section
- `Header.tsx` / `Footer.tsx` - Layout components
- `Sidebar.tsx` - Dashboard navigation
- `dashboard/*.tsx` - Dashboard-specific widgets
- `ui/*.tsx` - Reusable UI primitives

---

## 5. Configuration (`config/`)

Centralized configuration management with environment-specific overrides.

### Configuration Categories

| Directory      | Purpose                           |
|----------------|-----------------------------------|
| `ml/`          | Model parameters, data loader     |
| `production/`  | Production-specific settings      |
| `backtesting/` | Backtest configurations           |
| `cloudbuild/`  | CI/CD pipeline configurations     |

### Configuration Pattern

```yaml
# Conceptual configuration structure
environment: production

database:
  host: ${DB_HOST}
  pool_size: 10
  
features:
  cache_ttl: 300
  
model:
  version: latest
  timeout_ms: 100
```

---

## 6. Pipeline Orchestration (`dags/`)

Airflow DAGs for scheduled processing and workflow management.

### DAG Categories

- **Data pipelines**: Market data ingestion via REST APIs
- **Feature pipelines**: Feature computation and storage
- **Inference pipelines**: Model prediction workflows
- **Training pipelines**: Model retraining workflows
- **Maintenance**: Cleanup, archival, reports

---

## 7. Infrastructure Files

### Dockerfiles

Multiple Dockerfiles for different services:
- `Dockerfile` - Main platform
- `Dockerfile.final-gate` - ML inference service
- `Dockerfile.dashboard-api` - Backend API

### Cloud Build

CI/CD configurations for automated deployments:
- `cloudbuild-*.yaml` - Service-specific pipelines
- Multi-stage builds with testing

---

## Component Interactions

```
                     ┌─────────────┐
                     │    User     │
                     └──────┬──────┘
                            │
                     ┌──────▼──────┐
                     │  Dashboard  │
                     │  Frontend   │
                     └──────┬──────┘
                            │
                     ┌──────▼──────┐
                     │  Dashboard  │
                     │   Backend   │
                     └──────┬──────┘
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
┌───────▼───────┐   ┌───────▼───────┐   ┌───────▼───────┐
│    Trading    │   │   Execution   │   │   Database    │
│   Platform    │   │    Engine     │   │               │
│               │◀──│               │──▶│   Cloud SQL   │
│  (ML + Data)  │   │   (Orders)    │   │   + Redis     │
└───────┬───────┘   └───────────────┘   └───────────────┘
        │
        │
┌───────▼───────┐
│    Airflow    │
│  (Composer)   │
│               │
│  Orchestrates │
│  all DAGs     │
└───────────────┘
```

---

*Each component is designed for independent deployment and scaling while maintaining clear interfaces with other components.*
