import numpy as np

from matplotlib import pyplot

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

# Sample the domain without noise.
y = [objective(x, 0) for x in X]

# Sample the domain with noise.
ynoise = [objective(x) for x in X]

# Find best result.
ix = np.argmax(y)
print("Optima: x=%.3f, y=%.3f" % (X[ix], y[ix]))

# Plot the points with noise.
pyplot.scatter(X, ynoise)

# Plot the points without noise
pyplot.plot(X, y)
# show the plot
pyplot.show()
