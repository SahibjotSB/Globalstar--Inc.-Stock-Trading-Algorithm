# features/feature_engineering.py
import pandas as pd

def add_features(data):
    """Add temporal features for prediction."""
    data['Day'] = data['Date'].dt.day
    data['Month'] = data['Date'].dt.month
    data['Year'] = data['Date'].dt.year
    return data

def feature_engineering(data):
    """Prepare features and target for training."""
    X = data[['Day', 'Month', 'Year']]  # Temporal features
    y = data['Close_RBC']  # Target column
    return X, y
