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