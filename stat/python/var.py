import numpy as np
import pandas as pd
import statsmodels.api as sm

from statsmodels.tsa.api import VAR, DynamicVAR
from statsmodels.tsa.base.datetools import dates_from_str

"""
Vector autoregression (VAR var) for multiple time series along with Vector Error
Correction Models (VECM vecm).
"""

# Load and process data.
mdata = sm.datasets.macrodata.load_pandas().data
dates = mdata[["year", "quarter"]]
quarterly = dates["year"] + "Q" + dates["quarter"].astype(int).astype(str)
quarterly = dates_from_str(quarterly)
mdata.index = pd.DatetimeIndex(quarterly)
data = np.log(mdata).diff().dropna()

# Generate model.
model = VAR(data)
results = model.fit(2)
results.summary()
results.plot()
results.plot_acorr() # autocorrelation function

# Lag order selection
model.select_order(15) # Choice of lag order
results = model.fit(maxlags=15, ic="aic") # Fit to AIC

# Forecasting using linear predictor
lag_order = results.k_ar
results.forecast(data.values[-lag_order:], 5)
results.plot_forecast(10)

# Impulse response analysis
irf = results.irf(10)
irf.plot(orth=False)
