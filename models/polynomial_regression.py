from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import numpy as np

def train_model(X, y):
    """Train the polynomial regression model."""
    # Create polynomial features
    poly = PolynomialFeatures(degree=3)  # Adjust degree if needed
    X_poly = poly.fit_transform(X)

    # Fit model
    model = LinearRegression()
    model.fit(X_poly, y)

    return model, poly

def predict_future(model, poly, data, days_ahead):
    """Predict future stock prices."""
    # Get the last date in the dataset
    last_day = data.iloc[-1]

    # Create future dates
    future_dates = []
    for i in range(1, days_ahead + 1):
        future_dates.append([last_day['Day'] + i, last_day['Month'], last_day['Year']])

    # Transform the future dates and predict
    future_dates_poly = poly.transform(future_dates)
    future_predictions = model.predict(future_dates_poly)

    return future_predictions
