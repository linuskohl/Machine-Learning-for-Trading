import pandas as pd
import matplotlib.pyplot as plt
from util import get_data, plot_data, compute_daily_returns


def test_run():
    """Plot histograms"""
    start_date = '2009-01-01'
    end_date = '2012-12-31'
    dates = pd.date_range(start_date, end_date)
    symbols = ['SPY','XOM']

    df = get_data(symbols, dates)
    # Plot stocks
    plot_data(df)

    # Compute daily returns
    daily_returns = compute_daily_returns(df)
    plot_data(daily_returns, title="Daily returns")

    # Plot histograms same chart
    daily_returns['SPY'].hist(bins=20, label="SPY")
    daily_returns['XOM'].hist(bins=20, label="XOM")

    plt.legend(loc="upper left")
    plt.show()

if __name__ == "__main__":
    test_run()
