import matplotlib.pyplot as plt
import numpy as np
import pymc3 as pm
import pandas as pd
import theano

"""
Hierachical GLM.
"""

data = pd.read_csv(pm.get_data("radon.csv"))
data["log_radon"] = data["log_radon"].astype(theano.config.floatX)
county_names = data.county.unique()
county_idx = data.county_code.values

n_counties = len(data.county.unique())

# Unpooled (non-hierarchical model)

with pm.Model() as unpooled_model:

    # Independent parameters for each county
    a = pm.Normal("a", 0, sigma=100, shape=n_counties)
    b = pm.Normal("a", 0, sigma=100, shape=n_counties)

    # Model error
    eps = pm.HalfCauchy("eps", 5)

    # Model prediction of radon level
    # a[county_idx] translates to a[0, 0, 0, 1, 1, ...],
    # we thus link multiple household measures of a county
    # to its coefficients.
    radon_est = a[county_idx] + b[county_idx]*data.floor.values

    # Data likelihood
    y = pm.Normal('y', radon_est, sigma=eps, observed=data.log_radon)