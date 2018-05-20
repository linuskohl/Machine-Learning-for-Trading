import pandas as pd
import matplotlib.pyplot as plt
from util import get_data, plot_data, compute_daily_returns


def test_run():
    start_date = '2009-01-01'
    end_date = '2012-12-31'
    dates = pd.date_range(start_date, end_date)
    symbols = ['SPY']

    df = get_data(symbols, dates)
    daily_returns = compute_daily_returns(df)

    plot_data(daily_returns, title="Daily returns", ylabel="Daily returns")

    daily_returns.hist(bins=20)

    mean = daily_returns['SPY'].mean()
    print("mean:\t\t\t{}".format(mean))
    std = daily_returns['SPY'].std()
    print("std. deviation:\t{}".format(std))

    plt.axvline(mean, color='red',   linestyle='dashed', linewidth=1)
    plt.axvline(std,  color='black', linestyle='dashed', linewidth=1)
    plt.axvline(-std, color='black', linestyle='dashed', linewidth=1)

    plt.show()

    kurtosis = daily_returns.kurtosis()
    print("kurtosis:\t{}".format(kurtosis))

if __name__ == "__main__":
    test_run()
