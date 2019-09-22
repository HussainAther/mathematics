import numpy as np
import pymc3 as pm
import seaborn as sns
import matplotlib.pyplot as plt

"""
LKJ Cholesky prior distribution. Use the inverse-Wishart distribution as the conjugate prior
for the covariance matrix of a multivariate normal distribution. Good for modeling
the covariance matrix of a multivariate normal distribution.
"""

np.random.seed(1234)

N = 10000
muactual = np.array([1, -2])
sigmaactual = np.array([[.5, -.3], [-.3, 1.]])
x = np.random.multivariate_normal(muactual, sigmaactual, size=N)
