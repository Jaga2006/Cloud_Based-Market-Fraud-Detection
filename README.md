# Cloud_Based-Market-Fraud-Detection
## Overview
This project, developed as part of the Microsoft Elevate AICTE Internship, focuses on detecting market manipulation (e.g., wash trading, spoofing) using unsupervised machine learning. It is built to run on Microsoft Azure for high scalability and low latency.

## Architecture
1. **Ingestion**: Azure Event Hubs captures real-time market ticks.
2. **Processing**: Feature engineering (RSI, Moving Averages) using Pandas/PySpark.
3. **Detection**: Isolation Forest algorithm identifies anomalies.
4. **Deployment**: Model served via FastAPI in a Docker container on Azure Kubernetes Service (AKS).

## Setup
1. Clone the repo: `git clone <your-repo-url>`
2. Install dependencies: `pip install -r requirements.txt`
3. Run the API: `uvicorn src.app:app --reload`
