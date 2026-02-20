import pandas as pd
import numpy as np

def engineer_features(df):
    """
    Simulates feature engineering for market fraud detection.
    """
    # Calculate Price Change
    df['price_change'] = df['price'].diff()
    
    # Simple Moving Average
    df['sma_10'] = df['price'].rolling(window=10).mean()
    
    # Volatility (Rolling Std Dev)
    df['volatility'] = df['price'].rolling(window=10).std()
    
    # Detect Volume Spikes (e.g., 3x the average volume)
    df['volume_spike'] = df['volume'] > (df['volume'].rolling(window=20).mean() * 3)
    
    return df.fillna(0)
