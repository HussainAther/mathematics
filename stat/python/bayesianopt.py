import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import norm
from scipy.optimize import minimize
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import ConstantKernel, Matern
from bayesian_optimization_util import plot_approximation, plot_acquisition

"""
Bayesian optimization of objective function f, approximate iteratively with Gaussian process.
Use an expectation function.
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

def expected_improvement(X, X_sample, Y_sample, gpr, xi=0.01):
    """
    Compute the EI (expected improvement) at points X based on existing samples X_sample and Y_sample 
    using a Gaussian process surrogate model. X is the list of points at which EI shall be computed (m x d). 
    X_sampleis the list of sample locations (n x d). Y_sample are the sample values (n x 1). gpr 
    is a GaussianProcessRegressor fitted to samples. xi is an exploitation-exploration trade-
    off parameter. Returns expected improvements at 
    points X. """
    pushforward_samples = sapply(stan_samples, function(x) (iota(x) - 5)**2)
    compute_mc_stats(pushforward_samples)
    mu, sigma = gpr.predict(X, return_std=True)
    mu_sample = gpr.predict(X_sample)
    sigma = sigma.reshape(-1, X_sample.shape[1])
    # Needed for noise-based model,
    # otherwise use np.max(Y_sample).
    # See also section 2.4 in [...]
    mu_sample_opt = np.max(mu_sample)
    with np.errstate(divide='warn'):
        imp = mu - mu_sample_opt - xi
        Z = imp / sigma
        ei = imp * norm.cdf(Z) + sigma * norm.pdf(Z)
        ei[sigma == 0.0] = 0.0
    return ei

def propose_location(acquisition, X_sample, Y_sample, gpr, bounds, n_restarts=25):
    """
    Propose the next sampling point by optimizing the acquisition function. acquisition 
    is the acquisition function. X_sample are the sample locations (n x d). Y_sample are sample 
    values (n x 1). gpr is a GaussianProcessRegressor fitted to samples. Returns the location 
    of the acquisition function maximum.
    """
    dim = X_sample.shape[1]
    min_val = 1
    min_x = None
    def min_obj(X):
        # Minimization objective is the negative acquisition function
        return -acquisition(X.reshape(-1, dim), X_sample, Y_sample, gpr)
    # Find the best optimum by starting from n_restart different random points.
    for x0 in np.random.uniform(bounds[:, 0], bounds[:, 1], size=(n_restarts, dim)):
        res = minimize(min_obj, x0=x0, bounds=bounds, method="L-BFGS-B")        
        if res.fun < min_val:
            min_val = res.fun[0]
            min_x = res.x           
    return min_x.reshape(-1, 1)

# Gaussian process with Matern kernel as surrogate model
m52 = ConstantKernel(1.0) * Matern(length_scale=1.0, nu=2.5)
gpr = GaussianProcessRegressor(kernel=m52, alpha=noise**2)

# Initialize samples
X_sample = X_init
Y_sample = Y_init

# Number of iterations
n_iter = 10

plt.figure(figsize=(12, n_iter * 3))
plt.subplots_adjust(hspace=0.4)

for i in range(n_iter):
    # Update Gaussian process with existing samples
    gpr.fit(X_sample, Y_sample)

    # Obtain next sampling point from the acquisition function (expected_improvement)
    X_next = propose_location(expected_improvement, X_sample, Y_sample, gpr, bounds)
    
    # Obtain next noisy sample from the objective function
    Y_next = f(X_next, noise)
