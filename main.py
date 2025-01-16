import pandas as pd
from data.stock_data import fetch_data, preprocess_data
from features.feature_engineering import add_features
from models.polynomial_regression import train_model
from models.backtesting import backtest_strategy
from utils.plot import plot_stock_prices
from utils.metrics import calculate_sharpe_ratio, calculate_max_drawdown
import webbrowser
import os

# Fetch and preprocess data
ticker = 'RBC'
data = fetch_data(ticker, '2024-01-01', '2025-01-14')
data = preprocess_data(data)
data = add_features(data)

def open_html_popup():
    html_path = os.path.join(os.getcwd(), 'java', 'rbc_popup.html')
    
    webbrowser.open(f'file://{html_path}', new=2) 

# Model Trainer
X = data[['Day', 'Month', 'Year']]
y = data['Close']
model, poly = train_model(X, y)

latest_date = data['Date'].max()

# Future dates
future_dates = pd.date_range(start=latest_date + pd.Timedelta(days=1), end=latest_date + pd.Timedelta(days=5))

# Future
future_data = pd.DataFrame({
    'Day_': future_dates.day,
    'Month_': future_dates.month,
    'Year_': future_dates.year
})

# Poly Trans
X_future = poly.transform(future_data)

# Predict Future
predicted_prices = model.predict(X_future)

# Print 
for date, price in zip(future_dates, predicted_prices):
    print(f"Predicted price for {date.date()}: {price[0]:.2f}")


# Backtesting
strategy_returns = backtest_strategy(data, model, poly)

# Performance
sharpe_ratio = calculate_sharpe_ratio(strategy_returns)
max_drawdown = calculate_max_drawdown(strategy_returns)

# Results
print(f"Sharpe Ratio: {sharpe_ratio:.2f}")
print(f"Max Drawdown: {max_drawdown:.2f}")

# Plots
plot_stock_prices(data)
open_html_popup()
