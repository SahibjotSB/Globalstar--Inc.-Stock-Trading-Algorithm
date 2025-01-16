import pandas as pd
import plotly.graph_objects as go
import pandas as pd
import plotly.graph_objects as go

def plot_stock_prices(data):
    """Plot stock prices for RBC with a modern banking-style Plotly chart."""
    
    # Convert the Date_ column to datetime format
    data['Date_'] = pd.to_datetime(data['Date_'])
    
    # Filter data starting from 2024-01-01
    data = data[data['Date_'] >= '2024-01-01']
    
    # Create the figure
    fig = go.Figure()
    
    # Add traces for each price type with original line colors
    fig.add_trace(go.Scatter(x=data['Date_'], y=data['Open_RBC'], mode='lines', name='Open Price',
                             line=dict(color='royalblue', width=3, dash='dot')))  # Royal blue, dotted
    fig.add_trace(go.Scatter(x=data['Date_'], y=data['Close_RBC'], mode='lines', name='Close Price',
                             line=dict(color='darkorange', width=3)))  # Dark orange, solid
    fig.add_trace(go.Scatter(x=data['Date_'], y=data['High_RBC'], mode='lines', name='High Price',
                             line=dict(color='seagreen', width=3, dash='dash')))  # Sea green, dashed
    
    # Update layout for a clean, modern banking design
    fig.update_layout(
        title='Royal Bank of Canada (RBC) Stock Prices',
        xaxis_title='Date',
        yaxis_title='Price (USD)',
        template='plotly_dark',  # Dark background for a clean look
        plot_bgcolor='rgba(26, 31, 40, 1)',  # Dark background color for the plot area
        paper_bgcolor='rgba(26, 31, 40, 1)',  # Dark background for the entire paper
        title_font=dict(size=18, family='Helvetica Neue', color='white'),  # Clean and modern font
        xaxis=dict(
            showgrid=True, 
            gridwidth=0.5, 
            gridcolor='#3A3A3A', 
            tickangle=45, 
            ticks="outside",  # Add ticks for clarity
            tickfont=dict(family="Arial", size=12, color="white")
        ),
        yaxis=dict(
            showgrid=True, 
            gridwidth=0.5, 
            gridcolor='#3A3A3A',
            tickfont=dict(family="Arial", size=12, color="white")
        ),
        legend=dict(
            title='Price Type',
            title_font=dict(size=14, color='white'),
            font=dict(size=12, color='white')
        ),
        margin=dict(l=50, r=50, t=60, b=50),  # Add margins for better spacing
    )
    
    # Show the plot
    fig.show()


# import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
# import matplotlib.dates as mdates

# def plot_stock_prices(data):
#     """Plot stock prices for RBC with a modern, sleek look."""
    
#     # Convert the Date_ column to datetime format and set it as index
#     data['Date_'] = pd.to_datetime(data['Date_'])
#     data.set_index('Date_', inplace=True)
    
#     # Filter data starting from 2024-01-01
#     data = data[data.index >= '2024-01-01']
    
#     # Set the plot's appearance
#     sns.set_theme(style="whitegrid", palette="muted")
    
#     # Create the plot with a clean figure size
#     plt.figure(figsize=(12, 6))
    
#     # Plot each price type with distinct, modern styling
#     sns.lineplot(x=data.index, y=data['Open_RBC'], label='Open Price', color='royalblue', linewidth=2, linestyle='--')
#     sns.lineplot(x=data.index, y=data['Close_RBC'], label='Close Price', color='darkorange', linewidth=2)
#     sns.lineplot(x=data.index, y=data['High_RBC'], label='High Price', color='seagreen', linewidth=2, linestyle='-.')
    
#     # Formatting the x-axis with month ticks and ensuring date format
#     plt.gca().xaxis.set_major_locator(mdates.MonthLocator())  
#     plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))  
#     plt.gcf().autofmt_xdate()  # Auto format to avoid overlap of dates
    
#     # Adding title and labels with modern font styling
#     plt.title('Royal Bank of Canada (RBC) Stock Prices', fontsize=16, fontweight='bold', family='Arial')
#     plt.xlabel('Date', fontsize=12, family='Arial')
#     plt.ylabel('Price (USD)', fontsize=12, family='Arial')

#     # Enhance the background and grid for a modern look
#     plt.gca().set_facecolor('#f7f7f7')  # Light grey background
#     plt.grid(True, linestyle='--', linewidth=0.5, color='gray')
    
#     # Show legend with a more modern and concise font
#     plt.legend(title="Price Type", fontsize=10, title_fontsize=12)
    
#     # Show the plot
#     plt.show()
