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
