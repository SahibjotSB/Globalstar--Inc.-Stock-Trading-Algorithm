
import yfinance as yf

def fetch_data(ticker, start, end):
    """Download stock data."""
    data = yf.download(ticker, start=start, end=end)
    data['Date'] = data.index
    return data

def preprocess_data(data):
    """Add useful features like Day, Month, Year."""
    data['Day'] = data['Date'].dt.day
    data['Month'] = data['Date'].dt.month
    data['Year'] = data['Date'].dt.year
    return data
