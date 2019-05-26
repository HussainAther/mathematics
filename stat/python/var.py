import numpy as np
import pandas as pd
import statsmodels.api as sm

from statsmodels.tsa.api import VAR, DynamicVAR
from statsmodels.tsa.base.datetools import dates_from_str

"""
Vector autoregression (VAR var) for multiple time series along with Vector Error
Correction Models (VECM vecm).
"""

mdata = sm.datasets.macrodata.load_pandas().data
dates = mdata[["year", "quarter"]]
quarterly = dates["year"] + "Q" + dates["quarter"].astype(int).astype(str)
quarterly = dates_from_str(quarterly)
mdata.index = pd.DatetimeIndex(quarterly)
data = np.log(mdata).diff().dropna()
model = VAR(data)
