# Technology Overview

> Technologies used in the Disuza Quantitative platform.

---

## Programming Languages

### Python 3.12+

Primary language for the trading platform:

- **Data Processing**: pandas, numpy for numerical computing
- **Validation**: Pydantic for data validation and settings
- **Async**: asyncio for concurrent I/O operations
- **API**: FastAPI for REST services

**Key Libraries**:
- `pandas` / `numpy` - Data manipulation
- `lightgbm` - Gradient boosting models
- `scikit-learn` - ML utilities and K-Means clustering
- `fastapi` - API framework
- `pydantic` - Data validation
- `ccxt` - Exchange connectivity

### TypeScript

Frontend dashboard:

- React with hooks
- Next.js App Router
- TailwindCSS for styling

---

## Machine Learning

### Models

- **LightGBM** - Quantile regression for price prediction
- **K-Means** - Macro regime clustering
- **Ensemble** - Hierarchical gating with domain experts

### Training Infrastructure

```
Data (GCS) → Feature Engineering → Model Training (Vertex AI) → Artifacts (GCS)
```

- Cloud Storage for datasets and model artifacts
- Vertex AI for training and hyperparameter tuning
- Walk-forward validation for time-series

### Inference

- Containerized models on Cloud Run
- Batch inference via scheduled DAGs

---

## Data Infrastructure

### Data Sources

| Source Type        | Protocol  | Use Case                        |
|--------------------|-----------|--------------------------------|
| Exchange Data      | REST API  | Price, volume                  |
| On-Chain Analytics | REST API  | Network metrics, flows         |
| Macro Indicators   | REST API  | Regime classification          |
| Derivatives Data   | REST API  | Funding, open interest         |

### Storage

| Store          | Technology               | Purpose                        |
|----------------|--------------------------|--------------------------------|
| Operational DB | Cloud SQL (PostgreSQL)   | Positions, trades, state       |
| Cache          | Memorystore (Redis)      | Hot data, rate limiting        |
| Object Storage | Cloud Storage (GCS)      | Models, datasets, artifacts    |
| Message Queue  | Pub/Sub                  | Event distribution             |
| Document Store | Firestore                | Execution engine state         |

---

## Backend

### API Layer (FastAPI)

```python
# Conceptual structure

from fastapi import FastAPI, Depends
from pydantic import BaseModel

app = FastAPI(title="Disuza Operations API")

@app.get("/health")
async def health_check():
    return {"status": "healthy"}

@app.get("/positions")
async def get_positions(user: User = Depends(get_current_user)):
    # Returns current positions
    pass
```

Features:
- OpenAPI documentation
- Pydantic request validation
- JWT authentication

### Execution Engine

- Firestore for state management
- Pub/Sub for signal routing
- MT5 on Compute Engine for order execution

---

## Orchestration

### Apache Airflow (Cloud Composer)

All pipelines orchestrated through DAGs:

```python
# Conceptual DAG structure

from airflow import DAG
from airflow.operators.python import PythonOperator

with DAG('ml_inference_pipeline', schedule_interval='*/15 * * * *') as dag:
    fetch_data = PythonOperator(task_id='fetch_market_data', ...)
    compute_features = PythonOperator(task_id='compute_features', ...)
    run_inference = PythonOperator(task_id='run_inference', ...)
    
    fetch_data >> compute_features >> run_inference
```

### DAG Categories

| Category   | Purpose                | Schedule       |
|------------|------------------------|----------------|
| Data       | Market data ingestion  | Scheduled      |
| Features   | Feature computation    | After data     |
| Inference  | Model predictions      | After features |
| Training   | Model retraining       | On-demand      |

---

## Frontend

### Next.js 14

```
disuza-site/
├── app/
│   ├── layout.tsx
│   ├── page.tsx
│   └── dashboard/
│       ├── page.tsx
│       ├── analytics/
│       └── settings/
└── components/
```

- React with hooks
- TailwindCSS
- Deployed on Vercel (development)

---

## Infrastructure

### Docker

Services containerized:

```dockerfile
FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY src/ ./src/
CMD ["python", "-m", "src.main"]
```

### Cloud Build

CI/CD for container builds and deployments.

---

## Observability

### Logging

- Structured logging to Cloud Logging
- Telegram alerts for DAG failures and critical events

### Alerting

- Airflow DAG failure notifications
- Telegram bot for operational alerts

---

## Code Quality

- **Formatting**: Black
- **Testing**: pytest

---

## Secrets Management

Credentials stored in GCP Secret Manager:

```python
from google.cloud import secretmanager

def get_secret(secret_id: str) -> str:
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/{PROJECT_ID}/secrets/{secret_id}/versions/latest"
    response = client.access_secret_version(request={"name": name})
    return response.payload.data.decode("UTF-8")
```

---

*Built with AI assistance.*
