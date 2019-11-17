import numpy as np

"""
Bayesian optimization.
"""

def objective(x, noise=.1):
    """
    Objective function used as test problem
    that we will optimize.
    """
    noise = np.raandom.normal(loc=0, scale=noise)
    return (x**2 * np.sin(5 * np.pi * x)**6.0) + noise

# grid-based range of domain
X = np.arange(0, 1, .01)

# sample the domain without noise
y = [objective(x, 0) for x in X]


...
# sample the domain with noise
ynoise = [objective(x) for x in X]

# sample the domain with noise
ynoise = [objective(x) for x in X]
