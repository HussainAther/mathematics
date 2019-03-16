import os
import sys
import glob
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from scipy.optimize import minimize
from scipy.stats import bernoulli, binom
from IPython.display import Image
from numpy.core.umath_tests import matrix_multiply as mm

"""
We use the expectation-maximization (EM) algorithm to iterate over data
to find a maximum likelihood or maximum a posterior (MAP) estimate of parameters
for models affected by unobserved latent variables.
"""

def neg_loglik(thetas, n, xs, zs):
    """
    Use the negative log likelihood function to minimize it as part of
    a binomial theorem to get the maximum expectation.
    """
    return -np.sum([binom(n, thetas[z]).logpmf(x) for (x, z) in zip(xs, zs)])

m = 10
theta_A = 0.8
theta_B = 0.3
theta_0 = [theta_A, theta_B]

coin_A = bernoulli(theta_A)
coin_B = bernoulli(theta_B)

xs = map(sum, [coin_A.rvs(m), coin_A.rvs(m), coin_B.rvs(m), coin_A.rvs(m), coin_B.rvs(m)])
zs = [0, 0, 1, 0, 1]
