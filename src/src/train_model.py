import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib
from processing import engineer_features

def train():
    # Load sample data
    data = {
        'price': [100, 101, 102, 110, 100, 101, 150, 102, 101],
        'volume': [1000, 1100, 1050, 5000, 1020, 1100, 20000, 1050, 1100]
    }
    df = pd.DataFrame(data)
    df = engineer_features(df)
    
    # Train Isolation Forest
    model = IsolationForest(n_estimators=100, contamination=0.1, random_state=42)
    model.fit(df)
    
    # Save the model
    import os
    if not os.path.exists('models'):
        os.makedirs('models')
    joblib.dump(model, 'models/fraud_model.pkl')
    print("Model trained and saved to models/fraud_model.pkl")

if __name__ == "__main__":
    train()
