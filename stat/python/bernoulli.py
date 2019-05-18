import numpy as np
import pandas as pd
import statsmodels.api as sm
import sympy as sp
import pymc
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

from mpl_toolkits.mplot3d import Axes3D
from scipy import stats
from scipy.special import gamma
from sympy.interactive import printing

"""
Bayesian estimation of Bernoulli trials.
"""

np.random.seed(123)

# Simulate
nobs = 100
theta = 0.3
Y = np.random.binomial(1, theta, nobs)

# Plot
fig = plt.figure(figsize=(7,3))
gs = gridspec.GridSpec(1, 2, width_ratios=[5, 1]) 
ax1 = fig.add_subplot(gs[0])
ax2 = fig.add_subplot(gs[1])

ax1.plot(range(nobs), Y, "x")
ax2.hist(-Y, bins=2)

axn.yaxis.set(ticks=(0,1), ticklabels=("Failure", "Success"))
ax2.xaxis.set(ticks=(-1,0), ticklabels=("Success", "Failure"));

ax1.set(title=r"Bernoulli Trial Outcomes $(\theta=0.3)$", xlabel="Trial", ylim=(-0.2, 1.2))
ax2.set(ylabel="Frequency")

fig.tight_layout()
