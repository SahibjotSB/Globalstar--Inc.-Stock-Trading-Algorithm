import numpy as np

def backtest_strategy(data, model, poly):
    """Test the model's strategy."""
    data.columns = ['_'.join(col).strip() for col in data.columns.values]
    
    print(f"Columns in data: {data.columns}")  # Debug: Print column names
    
    if not all(col in data.columns for col in ['Day_', 'Month_', 'Year_']):
        raise ValueError("Data must contain 'Day_', 'Month_', and 'Year_' columns")

    data['Predicted_Close'] = model.predict(poly.transform(data[['Day_', 'Month_', 'Year_']]))

    data['Daily_Return'] = data['Close_RBC'].pct_change()

    print(data[['Predicted_Close', 'Close_RBC', 'Daily_Return']].head())

    data.reset_index(drop=True, inplace=True)

    try:
        data.dropna(subset=['Predicted_Close', 'Close_RBC', 'Daily_Return'], inplace=True)
    except KeyError as e:
        print(f"KeyError encountered: {e}")
        print(f"Data columns: {data.columns}")
        raise

    data['Strategy_Return'] = np.where(data['Predicted_Close'] > data['Close_RBC'], data['Daily_Return'], 0)
    
    return data['Strategy_Return']
