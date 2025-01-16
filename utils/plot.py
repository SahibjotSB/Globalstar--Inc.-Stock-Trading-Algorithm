# utils/plot.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates

def plot_stock_prices(data):
    """Plot stock prices."""
    
    # Convert the Date_ column to datetime format
    data['Date_'] = pd.to_datetime(data['Date_'])
    data.set_index('Date_', inplace=True)
    
    # Filter data starting from 2024-01-01
    data = data[data.index >= '2024-01-01']
    
    # Set the plot's appearance
    sns.set_theme(style="darkgrid")
    
    # Create the plot
    plt.figure(figsize=(12, 6))
    
    # Plot each price type with distinct styling
    sns.lineplot(x=data.index, y=data['Open_RBC'], label='Open Price', color='royalblue', linewidth=2, linestyle='--')
    sns.lineplot(x=data.index, y=data['Close_RBC'], label='Close Price', color='darkorange', linewidth=2)
    sns.lineplot(x=data.index, y=data['High_RBC'], label='High Price', color='green', linewidth=2, linestyle='-.')
    
    # Formatting the x-axis to show actual dates with month ticks
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator())  # Major tick every month
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))  # Date format
    plt.gcf().autofmt_xdate()  # Automatically format the dates to avoid overlap
    
    # Adding title and labels with font sizes
    plt.title('Royal Bank of Canada RBC Stock Prices', fontsize=16, fontweight='bold')
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Price (USD)', fontsize=12)

    # Enhancing legend appearance
    plt.legend(title="Price Type", fontsize=10, title_fontsize=12)
    
    # Display grid with light lines
    plt.grid(True, linestyle='--', linewidth=0.5)
    
    # Show plot
    plt.show()
