import numpy as np
import scipy.stats as st
import seaborn as sns
import matplotlib.pyplot as plt

"""
Using Markov Chain Monte Carlo methods, slice sampling lets us
use an adaptive step size that automaticaly adjusts to match the characteristics
of the distribution.
"""

sns.set()
mu = 65
sigma = 32

def p(x):
    """
    Partial differential function of the standard normal distribution.
    """
    return st.norm.pdf(x, loc=mu, scale=sigma)

def p_inv(y):
    """
    Inverse partial differential function of the normal distribution.
    """
    x = np.sqrt(-2*sigma**2 * np.log(y * sigma * np.sqrt(2*np.pi)))
    return mu-x, mu+x

def slice_sampling(iter=1000):
    """
    Slice sampling method.
    1. Set a starting point x
    2. Sample the height u ~ Unif(0, p(x))
    3. Sample the next x ~ Unif(-z, z), where z is the inverse PDF evaluated at u
    4. Go to step 2
    """
    samples = np.zeros(iter)
    x = 0

    for i in range(iter):
        u = np.random.uniform(0, p(x))
        x_lo, x_hi = p_inv(u)
        x = np.random.uniform(x_lo, x_hi)
        samples[i] = x

    return samples
