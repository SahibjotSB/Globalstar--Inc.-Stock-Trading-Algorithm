
def calculate_sharpe_ratio(strategy_returns):
    """Calculate Sharpe ratio."""
    return strategy_returns.mean() / strategy_returns.std() * np.sqrt(252)

def calculate_max_drawdown(strategy_returns):
    """Calculate max drawdown."""
    cumulative_returns = (1 + strategy_returns).cumprod()
    drawdown = cumulative_returns / cumulative_returns.cummax() - 1
    return drawdown.min()
