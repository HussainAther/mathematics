import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import norm

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
    using a Gaussian process surrogate model. Args: X: Points at which EI shall be computed (m x d). 
    X_sample: Sample locations (n x d). Y_sample: Sample values (n x 1). gpr: A GaussianProcessRegressor 
    fitted to samples. xi: Exploitation-exploration trade-off parameter. Returns: Expected improvements at 
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
