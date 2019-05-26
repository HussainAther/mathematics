import numpy as np
import statsmodels.api as sm

from scipy import stats
from statsmodels.graphics.api import abline_plot
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

# Hold explanatory variables constant at their means and manipulate the percentage
# of low income households to find its impact on response
means = data.exog.mean(axis=0)
means25 = means.copy()
means25[0] = stats.scoreatpercentile(data.exog[:,0], 25)
means75 = means.copy()
means75[0] = lowinc_75per = stats.scoreatpercentile(data.exog[:,0], 75)
resp_25 = res.predict(means25)
resp_75 = res.predict(means75)
diff = resp_75 - resp_25

# Interquartile first difference fro percentage of low income households
print("%2.4f%%" % (diff*100))

# Plot
nobs = res.nobs
y = data.endog[:,0]/data.endog.sum(1)
yhat = res.mu
fig, ax = plt.subplots()
ax.scatter(yhat, y)
line_fit = sm.OLS(y, sm.add_constant(yhat, prepend=True)).fit()
abline_plot(model_results=line_fit, ax=ax)
ax.set_title("Model Fit Plot")
ax.set_ylabel("Observed values")
ax.set_xlabel("Fitted values")

# Residuals
fig, ax = plt.subplots()
ax.scatter(yhat, res.resid_pearson)
ax.hlines(0, 0, 1)
ax.set_xlim(0, 1)
ax.set_title("Residual Dependence Plot")
ax.set_ylabel("Pearson Residuals")
ax.set_xlabel("Fitted values")
