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
    return -np.sum([binom(n, thetas[z]).logpmf(x) for (x, z) in zip(xs, zs)])
