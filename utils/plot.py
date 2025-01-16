
import matplotlib.pyplot as plt
import seaborn as sns

def plot_stock_prices(data):
    """Plot stock prices."""
    plt.figure(figsize=(10, 6))
    sns.lineplot(x=data.index, y=data['Open'], label='Open Price')
    sns.lineplot(x=data.index, y=data['Close'], label='Close Price')
    sns.lineplot(x=data.index, y=data['High'], label='High Price')
    plt.title('GSAT Stock Prices')
    plt.xlabel('Date')
    plt.ylabel('Price (USD)')
    plt.legend()
    plt.grid(True)
    plt.show()
