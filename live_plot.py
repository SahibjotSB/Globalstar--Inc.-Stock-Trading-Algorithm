# import pandas as pd
# import time
# from datetime import datetime, timedelta
# import plotly.graph_objs as go
# from plotly.subplots import make_subplots
# from data.stock_data import fetch_data, preprocess_data
# from models.polynomial_regression import train_model, predict_future

# def live_plot(ticker, start_date, end_date, prediction_days=5, interval=10):
#     """
#     Live plot historical and predicted stock prices.
    
#     Args:
#         ticker (str): Stock ticker symbol.
#         start_date (str): Start date for historical data in 'YYYY-MM-DD' format.
#         end_date (str): End date for historical data in 'YYYY-MM-DD' format.
#         prediction_days (int): Number of days to predict into the future.
#         interval (int): Refresh interval in seconds.
#     """
#     # Fetch and preprocess data
#     data = fetch_data(ticker, start_date, end_date)
#     data = preprocess_data(data)

#     # Train the model
#     model, poly = train_model(data['Day'].values.reshape(-1, 1), data['Close'].values)

#     # Set up the Plotly figure
#     fig = make_subplots(specs=[[{"secondary_y": True}]])
#     fig.update_layout(
#         title=f"Live Stock Prices and Predictions for {ticker}",
#         xaxis_title="Date",
#         yaxis_title="Stock Price (USD)",
#         template="plotly_white",
#     )

#     while True:
#         # Predict future prices
#         future_dates, predicted_prices = predict_future(data, days_ahead=prediction_days, poly=poly, model=model)

#         # Update the figure with historical data
#         fig.data = []  # Clear previous traces
#         fig.add_trace(
#             go.Scatter(
#                 x=data['Date'],
#                 y=data['Close'],
#                 mode='lines',
#                 name="Historical Close Prices",
#                 line=dict(color='blue'),
#             )
#         )

#         # Add predicted prices to the plot
#         fig.add_trace(
#             go.Scatter(
#                 x=future_dates,
#                 y=predicted_prices,
#                 mode='lines',
#                 name="Predicted Prices",
#                 line=dict(color='orange', dash='dash'),
#             )
#         )

#         # Show the plot
#         fig.show(renderer="browser")

#         # Pause before updating
#         time.sleep(interval)
#         end_date = (datetime.strptime(end_date, '%Y-%m-%d') + timedelta(days=1)).strftime('%Y-%m-%d')


# if __name__ == "__main__":
#     # Example usage
#     ticker = "RY.TO"  # RBC stock ticker
#     start_date = "2024-01-01"
#     end_date = datetime.now().strftime('%Y-%m-%d')
#     live_plot(ticker, start_date, end_date, prediction_days=5, interval=10)
