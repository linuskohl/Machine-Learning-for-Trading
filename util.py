import os
import pandas as pd
import matplotlib.pyplot as plt

def symbol_to_path(symbol, base_dir="sample_data"):
    """Get path of file containing data of symbol."""
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def get_data(symbols, dates):
    """Load data of symbols in symbols array."""
    df = pd.DataFrame(index=dates)
    if 'SPY' not in symbols:
        symbols.insert(0, 'SPY')

    for symbol in symbols:
        df_tmp = pd.read_csv(symbol_to_path(symbol), index_col="Date",
                             parse_dates=True,
                             usecols=['Date', 'Adj Close'],
                             na_values='nan')
        df_tmp = df_tmp.rename(columns={'Adj Close': symbol})
        df = df.join(df_tmp)
        if symbol == 'SPY':
            df = df.dropna(subset=['SPY'])

    return df


def fill_missing_values(df_data):
    """Fill missing values in data frame (in place)"""
    # At first fill missing data forward
    df_data.fillna(method='ffill', inplace=True)
    # Fill the rest backwards
    df_data.fillna(method='bfill', inplace=True)


def noramlize_data(df):
    """Normalize data"""
    return df/df.ix[0,:]

def get_rolling_mean(df, window):
    """Get the rolling mean"""
    return pd.Series(df).rolling(window=window).mean()

def get_rolling_std(df, window):
    """Get the rolling standard deviation"""
    return pd.Series(df).rolling(window=window).std()

def get_bollinger_bands(rm_df, rstd_df):
    """Get Bollinger Bands (R)"""
    upper_band = rm_df + rstd_df * 2
    lower_band = rm_df - rstd_df * 2
    return (upper_band, lower_band)

def compute_daily_returns(df):
    """Compute and return the daily return values."""
    daily_returns = df.copy()
    daily_returns[1:] = (df[1:]/df[:-1].values) - 1
    daily_returns.ix[0, :] = 0
    return daily_returns

def plot_data(df, title="Stock prices", xlabel="Date", ylabel="Price"):
    """Plots the data"""
    ax = df.plot(title=title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    plt.show()

def plot_selected(df, columns, start_index, end_index):
    df_tmp = df.ix[start_index:end_index,columns]
    plot_data(df_tmp)
