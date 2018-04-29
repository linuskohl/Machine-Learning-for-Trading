import os
import pandas as pd
import matplotlib.pyplot as plt

def symbol_to_path(symbol, base_dir="data"):
    return os.path.join(base_dir, "{}.csv".format(str(symbol)))

def get_data(symbols, dates):
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

def noramlize_data(df):
    return df/df.ix[0,:]

def plot_data(df, title="Stock prices"):
    ax = df.plot(title=title)
    ax.set_xlabel("Date")
    ax.set_ylabel("Price")
    plt.show()

def plot_selected(df, columns, start_index, end_index):
    df_tmp = df.ix[start_index:end_index,columns]
    plot_data(df_tmp)

def test_run():
    start_date='2010-01-01'
    end_date='2010-12-31'
    dates=pd.date_range(start_date, end_date)
    symbols=['GOOG','IBM','GLD']

    df1 = get_data(symbols, dates)
    df1 = noramlize_data(df1)

    plot_selected(df1, ['SPY','GOOG','IBM','GLD'], "2010-01-01", "2010-12-31")

if __name__ == "__main__":
    test_run()
