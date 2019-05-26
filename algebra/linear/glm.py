import numpy as np
import statsmodels.api as sm

from scipy import stats
from matplotlib import pyplot as plt

"""
Generalized linear model (glm GLM)
"""

# Load data
data = sm.datasets.star98.load(as_pandas=False)
data.exog = sm.add_constant(data.exog, prepend=False)

# Fit and print
glm_binom = sm.GLM(data.endog, data.exog, family=sm.families.Binomial())
res = glm_binom.fit()
print(res.summary())
print("Total number of trials:",  data.endog[0].sum())
print("Parameters: ", res.params)
print("T-values: ", res.tvalues)
