from fastapi import FastAPI
import joblib
import pandas as pd
from .processing import engineer_features

app = FastAPI(title="Cloud Fraud Detection API")

# Load model on startup
model = joblib.load('models/fraud_model.pkl')

@app.get("/")
def home():
    return {"status": "Online", "system": "Market Fraud Detection"}

@app.post("/predict")
def predict_fraud(data: list):
    """
    Receives a list of transaction objects and returns fraud scores.
    Input: [{"price": 100, "volume": 1200}, ...]
    """
    df = pd.DataFrame(data)
    processed_df = engineer_features(df)
    
    # -1 for anomaly (fraud), 1 for normal
    predictions = model.predict(processed_df)
    
    results = []
    for i, pred in enumerate(predictions):
        status = "Fraudulent" if pred == -1 else "Normal"
        results.append({"transaction_id": i, "status": status})
        
        return {"results": results}
