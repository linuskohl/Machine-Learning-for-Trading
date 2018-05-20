import os
import pandas as pd
import matplotlib.pyplot as plt
from util import *

def test_run():
    start_date='2005-12-31'
    end_date='2014-12-07'
    dates=pd.date_range(start_date, end_date)
    symbols=['JAVA','FAKE1','FAKE2','SPY']

    df = get_data(symbols, dates)

    plot_data(df, "data")

if __name__ == "__main__":
    test_run()
