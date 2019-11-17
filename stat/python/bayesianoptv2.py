import numpy as np

from matplotlib import pyplot
from sklearn.gaussian_process import GaussianProcessRegressor

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

def surrogate(model, X):
    """
    Surrogate (approximation) of the objective function that we use
    in plotting to make sure we catch warnings.
    """
    # catch any warning generated when making a prediction
    with catch_warnings():
        # ignore generated warnings
        simplefilter("ignore")
        return model.predict(X, return_std=True)

# plot real observations vs surrogate function
def plot(X, y, model):
    """
    Plot the real function and the surrogate function.
    """
    # scatter plot of inputs and real objective function
    pyplot.scatter(X, y)
    # line plot of surrogate function across domain
    Xsamples = np.asarray(np.arange(0, 1, 0.001))
    Xsamples = Xsamples.reshape(len(Xsamples), 1)
    ysamples, _ = surrogate(model, Xsamples)
    pyplot.plot(Xsamples, ysamples)
    # Show the plot.
    pyplot.show()
