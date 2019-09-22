import numpy as np
import pymc3 as pm
import seaborn as sns
import matplotlib.pyplot as plt

"""
LKJ prior distribution. Use the inverse-Wishart distribution as the conjugate prior
for the covariance matrix of a multivariate normal distribution. Good for modeling
the covariance matrix of a multivariate normal distribution.
"""
