<div align="center">

# Disuza Quantitative

### Institutional-Grade Algorithmic Trading Infrastructure

[![Python](https://img.shields.io/badge/Python-3.12+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0+-3178C6?style=for-the-badge&logo=typescript&logoColor=white)](https://typescriptlang.org)
[![GCP](https://img.shields.io/badge/Google_Cloud-Production-4285F4?style=for-the-badge&logo=googlecloud&logoColor=white)](https://cloud.google.com)
[![License](https://img.shields.io/badge/License-Apache_2.0-blue?style=for-the-badge)](LICENSE)

*A production-grade quantitative trading system processing market data through machine learning pipelines orchestrated by Apache Airflow for autonomous execution across multiple venues.*

---

[Architecture](#system-architecture) • [Technology](#technology-stack) • [Components](#core-components) • [Infrastructure](#infrastructure) • [Contact](#contact)

</div>

---

## Overview

Disuza Quantitative is a fully autonomous algorithmic trading infrastructure designed for institutional-level reliability and performance. The system integrates data ingestion, machine learning inference, risk management, and multi-venue execution into a unified, cloud-native platform orchestrated by Apache Airflow on Google Cloud Composer.

> **Note**: This repository serves as a portfolio showcase. All proprietary trading logic, model implementations, feature engineering, and alpha-generating code remain private.

### Key Capabilities

- **Pipeline Orchestration**: Apache Airflow on Cloud Composer for reliable workflow management
- **Multi-Asset Support**: Cryptocurrency markets with multi-venue execution
- **Machine Learning Pipeline**: Ensemble models with hierarchical gating architecture
- **Risk Management**: Position monitoring, drawdown controls, and exposure limits
- **Observability**: Comprehensive logging, metrics, and alerting infrastructure

---

## System Architecture

```
┌──────────────────────────────────────────────────────────────────────────────────┐
│                               DISUZA QUANTITATIVE                                │
│                          Algorithmic Trading Platform                            │
├──────────────────────────────────────────────────────────────────────────────────┤
│                                                                                  │
│  ┌──────────────────┐    ┌──────────────────┐    ┌──────────────────┐            │
│  │    DATA LAYER    │    │     ML LAYER     │    │  EXECUTION LAYER │            │
│  │                  │    │                  │    │                  │            │
│  │  • Market Data   │───▶│  • Feature Eng   │───▶│  • Risk Manager  │            │
│  │  • On-Chain Data │    │  • Model Infer   │    │  • Order Router  │            │
│  │  • Macro Data    │    │  • Signal Gen    │    │  • Position Mgmt │            │
│  │  • Derivatives   │    │  • Ensemble      │    │  • Multi-Venue   │            │
│  └──────────────────┘    └──────────────────┘    └──────────────────┘            │
│            │                      │                       │                      │
│            ▼                      ▼                       ▼                      │
│  ┌──────────────────────────────────────────────────────────────────┐            │
│  │                    ORCHESTRATION LAYER                           │            │
│  │                                                                  │            │
│  │        Apache Airflow (Cloud Composer) │ DAGs │ Scheduling       │            │
│  └──────────────────────────────────────────────────────────────────┘            │
│            │                      │                       │                      │
│            ▼                      ▼                       ▼                      │
│  ┌──────────────────────────────────────────────────────────────────┐            │
│  │                    INFRASTRUCTURE LAYER                          │            │
│  │                                                                  │            │
│  │    Cloud SQL │ Redis │ Pub/Sub │ Cloud Run │ Cloud Build │ IAM   │            │
│  └──────────────────────────────────────────────────────────────────┘            │
│                                                                                  │
│  ┌──────────────────────────────────────────────────────────────────┐            │
│  │                    MONITORING & OPERATIONS                       │            │
│  │                                                                  │            │
│  │     Dashboard │ Alerting │ Logging │ Metrics │ Audit Trail       │            │
│  └──────────────────────────────────────────────────────────────────┘            │
│                                                                                  │
└──────────────────────────────────────────────────────────────────────────────────┘
```

### Data Flow Architecture

```
Market Data Sources              Orchestration & Processing                 Execution
───────────────────             ──────────────────────────                 ──────────

┌─────────────────┐            ┌─────────────────────────┐              ┌───────────┐
│    Exchange     │────REST───▶│   Apache Airflow DAGs   │              │    MT5    │
│      APIs       │            │   (Cloud Composer)      │              │   Broker  │
└─────────────────┘            └───────────┬─────────────┘              └─────▲─────┘
                                           │                                  │
┌─────────────────┐            ┌───────────▼─────────────┐  ┌──────────┐      │
│    On-Chain     │────REST───▶│   Feature Engineering   │─▶│  Signal  │──────┤
│    Providers    │            │   & ML Inference        │  │  Router  │      │
└─────────────────┘            └───────────┬─────────────┘  └──────────┘      │
                                           │                                  │
┌─────────────────┐            ┌───────────▼─────────────┐              ┌─────▼─────┐
│      Macro      │────REST───▶│   Cloud Run Functions   │              │  CEX/DEX  │
│     Sources     │            │   (Inference Engines)   │              │   Venues  │
└─────────────────┘            └─────────────────────────┘              └───────────┘
```

---

## Technology Stack

### Core Technologies


| Layer              | Technologies                               |
| ------------------ | ------------------------------------------ |
| **Languages**      | Python 3.12+, TypeScript 5.0+, SQL         |
| **ML/Data**        | LightGBM, Pandas, NumPy, Scikit-learn      |
| **Backend**        | FastAPI, asyncio, Pydantic                 |
| **Frontend**       | Next.js 14, React 18, TailwindCSS          |
| **Databases**      | PostgreSQL (Cloud SQL), Redis              |
| **Orchestration**  | Apache Airflow (Cloud Composer), Pub/Sub   |
| **Infrastructure** | Google Cloud Platform, Docker, Cloud Build |

### GCP Services Utilized

- **Orchestration**: Cloud Composer (Managed Apache Airflow), Cloud Scheduler
- **Compute**: Cloud Run, Compute Engine (Windows Server for MT5 Execution)
- **Data**: Cloud SQL (PostgreSQL), Cloud Storage (GCS), Memorystore (Redis)
- **Messaging**: Pub/Sub for pipeline communication
- **ML Platform**: Vertex AI (Training & Hyperparameter Tuning)
- **Security**: Secret Manager, Firestore
- **CI/CD**: Cloud Build, Artifact Registry

### Development Practices

- **Architecture**: DAG-based pipelines with clear domain boundaries
- **Code Quality**: Type hints, comprehensive docstrings, linting (Ruff)
- **Configuration**: YAML-based configuration management with environment overrides
- **Deployment**: Immutable infrastructure with containerized services
- **Monitoring**: Structured logging, custom metrics, automated alerting

---

## Core Components

### 1. ML Training & Inference Platform

*Production machine learning pipeline for model training, validation, and inference*

- Hierarchical gating architecture with specialized expert models
- Automated hyperparameter optimization with Vertex AI
- Rolling validation with walk-forward analysis
- Feature versioning and experiment tracking

### 2. Execution Engine

*Multi-venue order execution with intelligent routing and risk controls*

- Unified interface for multiple exchange protocols (REST APIs)
- Multi-account parallel execution with SQL state management
- Real-time dashboard communication and configuration sync
- Position and exposure management across venues
- P&L tracking and drawdown monitoring
- Telegram notifications for trade alerts and system status

### 3. Data Pipeline

*Batch and scheduled data processing infrastructure*

- REST API connections for market data ingestion
- Technical indicator computation engine
- On-chain data integration (blockchain analytics)
- Macro regime classification

### 4. Operations Dashboard

*Monitoring and control interface*

- Live position and P&L visualization
- Trade execution history and analytics
- System health monitoring
- Configuration management

---

## Infrastructure

### Deployment

- **Region**: europe-west4 (GCP) with europe-west1 redundancy
- **Execution Engine**: Compute Engine Windows Server (MT5)
- **Services**: Cloud Run containerized deployments
- **Orchestration**: Cloud Composer managed Airflow

### Security

- Secrets management via GCP Secret Manager
- Service accounts for authentication
- Encrypted credentials storage

---

## Project Structure

```
disuza-quantitative/
│
├── src/                          # Core trading platform
│   ├── core/                     # Shared infrastructure (messaging, state)
│   ├── data_pipeline/            # Market data ingestion & processing
│   ├── features/                 # Feature engineering engine
│   ├── ML/                       # Model training & inference
│   ├── ml_pipelines/             # Pipeline orchestration
│   ├── functions/                # Cloud Run service deployments
│   └── utils/                    # Shared utilities
│
├── trading-execution-engine/     # Order execution system
│   ├── src/
│   │   ├── core/                 # Configuration & data models
│   │   ├── dispatcher/           # Signal routing
│   │   ├── execution/            # Venue-specific executors
│   │   └── workers/              # Background processors
│   └── external-watchdog/        # Health monitoring service
│
├── disuza-dashboard-backend/     # Operations API
│   ├── routers/                  # API endpoints
│   └── services/                 # Business logic
│
├── disuza-site/                  # Web dashboard (Next.js)
│   ├── app/                      # Pages & layouts
│   └── components/               # React components
│
├── config/                       # Configuration files
│   ├── ml/                       # Model configurations
│   ├── production/               # Production settings
│   └── backtesting/              # Backtest parameters
│
├── dags/                         # Airflow DAGs (pipeline orchestration)
│   ├── scripts/                  # DAG helper scripts & job submissions
│   └── pipelines/                # Pipeline definitions
│
└── docs/                         # Technical documentation
```

---

## System Capabilities

- **Fault Tolerance**: Automatic retry with exponential backoff, graceful degradation
- **Observability**: Structured logging, Cloud Monitoring metrics, Telegram alerts
- **Scalability**: Stateless services, horizontal scaling via Cloud Run
- **Reliability**: DAG-based orchestration with dependency tracking

---

## Skills Demonstrated

This project showcases expertise in:

- **System Design**: Distributed systems, pipeline architecture, microservices
- **Machine Learning**: Production ML pipelines, model serving, feature engineering
- **Cloud Engineering**: GCP services, infrastructure as code, CI/CD
- **Software Engineering**: Python best practices, async programming, API design
- **Financial Engineering**: Market microstructure, execution algorithms, risk management
- **DevOps**: Containerization, monitoring, logging, alerting
- **Full-Stack Development**: React, Next.js, FastAPI, PostgreSQL

---

## Documentation

Detailed documentation is available in the [`docs/`](docs/) folder:

- [Architecture Overview](docs/ARCHITECTURE.md)
- [Technology Deep Dive](docs/TECHNOLOGY.md)
- [Component Details](docs/COMPONENTS.md)
- [Skills Matrix](docs/SKILLS.md)
- [FAQ](docs/FAQ.md)

---

## Contact

<div align="center">

**Disuza Quantitative**

Building the future of systematic trading.

[![Website](https://img.shields.io/badge/Website-disuza.com-000000?style=for-the-badge)](https://disuza.com)
[![Email](https://img.shields.io/badge/Email-contact%40disuza.com-D14836?style=for-the-badge&logo=gmail&logoColor=white)](mailto:contact@disuza.com)

</div>

---

<div align="center">

*This repository is a portfolio showcase. All proprietary trading logic, algorithms, and alpha-generating code are maintained in private repositories.*

**© 2025-2026 Disuza Quantitative. All rights reserved.**

</div>
