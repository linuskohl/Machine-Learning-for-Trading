import os
import pandas as pd
import matplotlib.pyplot as plt
from util import *


def test_run():
    start_date = '2010-01-01'
    end_date = '2010-12-31'
    dates = pd.date_range(start_date, end_date)
    symbols = ['SPY', 'FAKE1']

    df = get_data(symbols, dates)

    # Plot SPY
    ax = df['SPY'].plot(title="SPY rolling mean", label='SPY')

    # Compute rolling mean
    rm_SPY = get_rolling_mean(df['SPY'], 20)

    # Compute rolling standard deviation
    std_SPY = get_rolling_std(df['SPY'], 20)

    # Bands
    upper_bollinger_band, lower_bollinger_band = get_bollinger_bands(rm_SPY, std_SPY)

    # Add rolling mean to plot
    rm_SPY.plot(label="Rolling mean", ax=ax)

    upper_bollinger_band.plot(label="Upper Bolliner band", ax=ax)
    lower_bollinger_band.plot(label="Lower Bolliner band", ax=ax)

    # Add details to plot
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    ax.legend(loc='upper left')

    # Display the graph
    plt.show()

    #
    dr = compute_daily_returns(df)
    print(dr)


if __name__ == "__main__":
    test_run()
