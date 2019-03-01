from __future__ import division
import pandas as pd
from numpy.random import randn
import numpy as np
pd.options.display.max_rows = 12
np.set_printoptions(precision=4, suppress=True)
import matplotlib.pyplot as plt
plt.rc('figure', figsize=(12, 6))
from pandas_datareader import data, wb

"""
A simplified cross-sectional momentum portfolio and a grid of model parameterizations.
"""

names = ['AAPL', 'GOOG', 'MSFT', 'DELL', 'GS', 'MS', 'BAC', 'C']

def get_px(stock, start, end):
    return web.get_data_yahoo(stock, start, end)["Adj Close"]

px = pd.DataFrame({n: get_px(n, '1/1/2009', '6/1/2012') for n in names})

def calc_mom(price, lookback, lag):
    mom_ret = price.shift(lag).pct_change(lookback)
    ranks = mom_ret.rank(axis=1, ascending=False)
    demeaned = ranks - ranks.mean(axis=1)
    return demeaned / demeaned.std(axis=1)

compound = lambda x : (1 + x).prod() - 1
daily_sr = lambda x: x.mean() / x.std()
