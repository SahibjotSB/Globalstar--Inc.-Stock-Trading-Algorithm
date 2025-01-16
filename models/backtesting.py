import numpy as np

def backtest_strategy(data, model, poly):
    """Test the model's strategy."""
    # Flatten MultiIndex columns
    data.columns = ['_'.join(col).strip() for col in data.columns.values]
    
    # Debug: Print the column names to ensure 'Day_', 'Month_', 'Year_' are present
    print(f"Columns in data: {data.columns}")  # Debug: Print column names
    
    # Ensure the 'Day_', 'Month_', and 'Year_' columns are present before transformation
    if not all(col in data.columns for col in ['Day_', 'Month_', 'Year_']):
        raise ValueError("Data must contain 'Day_', 'Month_', and 'Year_' columns")

    # Predict stock prices using the model and polynomial transformation
    data['Predicted_Close'] = model.predict(poly.transform(data[['Day_', 'Month_', 'Year_']]))

    # Calculate daily returns
    data['Daily_Return'] = data['Close_GSAT'].pct_change()

    # Debug: Print the first few rows of data to ensure columns exist
    print(data[['Predicted_Close', 'Close_GSAT', 'Daily_Return']].head())

    # Reset index to prevent issues with multi-index or complex index
    data.reset_index(drop=True, inplace=True)

    # Drop any rows with missing values in the relevant columns
    try:
        data.dropna(subset=['Predicted_Close', 'Close_GSAT', 'Daily_Return'], inplace=True)
    except KeyError as e:
        print(f"KeyError encountered: {e}")
        print(f"Data columns: {data.columns}")
        raise

    # Compute strategy returns: if predicted price is higher than current price, use the daily return; otherwise 0
    data['Strategy_Return'] = np.where(data['Predicted_Close'] > data['Close_GSAT'], data['Daily_Return'], 0)
    
    return data['Strategy_Return']
