import numpy as np
import matplotlib.pyplot as plt

"""
Bayesian optimization of objective function f, approximate iteratively with Gaussian process.
"""

bounds = np.array([[-1.0, 2.0]])
noise = 0.2

def f(X, noise=noise):
    """
    Function to optimize.
    """
    return -np.sin(3*X) - X**2 + 0.7*X + noise * np.random.randn(*X.shape)

X_init = np.array([[-0.9], [1.1]])
Y_init = f(X_init)
