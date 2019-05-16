import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import norm

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

# Dense grid of points within bounds
X = np.arange(bounds[:, 0], bounds[:, 1], 0.01).reshape(-1, 1)

# Noise-free objective function values at X 
Y = f(X,0)

# Plot optimization objective with noise level 
plt.plot(X, Y, "y--", lw=2, label="Noise-free objective")
plt.plot(X, f(X), "bx", lw=1, alpha=0.1, label="Noisy samples")
plt.plot(X_init, Y_init, "kx", mew=3, label="Initial samples")
plt.legend()

