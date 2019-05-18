import numpy as np
import pandas as pd
import statsmodels.api as sm
import sympy as sp
import pymc
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

from mpl_toolkits.mplot3d import Axes3D
from scipy import stats
from scipy.special import gamma
from sympy.interactive import printing
from libc.math cimport pow

cimport numpy as np
cimport cython

"""
Bayesian estimation of Bernoulli trials.
"""

np.random.seed(123)

# Simulate Bernoulli trials
nobs = 100
theta = 0.3
Y = np.random.binomial(1, theta, nobs)

# Plot
fig = plt.figure(figsize=(7,3))
gs = gridspec.GridSpec(1, 2, width_ratios=[5, 1]) 
ax1 = fig.add_subplot(gs[0])
ax2 = fig.add_subplot(gs[1])
ax1.plot(range(nobs), Y, "x")
ax2.hist(-Y, bins=2)
axn.yaxis.set(ticks=(0,1), ticklabels=("Failure", "Success"))
ax2.xaxis.set(ticks=(-1,0), ticklabels=("Success", "Failure"));
ax1.set(title=r"Bernoulli Trial Outcomes $(\theta=0.3)$", xlabel="Trial", ylim=(-0.2, 1.2))
ax2.set(ylabel="Frequency")
fig.tight_layout()

# Bayesian estimation using likelihood function
t, T, s = sp.symbols('theta, T, s')

# Create the function symbolically
likelihood = (t**s)*(1-t)**(T-s)

# Convert it to a Numpy-callable function
_likelihood = sp.lambdify((t,T,s), likelihood, modules="numpy")

# Prior
# For alpha_1 = alpha_2 = 1, the Beta distribution
# degenerates to a uniform distribution
a1 = 1
a2 = 1

# Prior Mean
prior_mean = a1 / (a1 + a2)
print("Prior mean:", prior_mean)

# Plot the prior
fig = plt.figure(figsize=(10,4))
ax = fig.add_subplot(111)
X = np.linspace(0,1, 1000)
ax.plot(X, stats.beta(a1, a2).pdf(X), "g")

# Cleanup
ax.set(title="Prior Distribution", ylim=(0,12))
ax.legend(["Prior"])

# Posterior
# Find the hyperparameters of the posterior
a1_hat = a1 + Y.sum()
a2_hat = a2 + nobs - Y.sum()

# Posterior Mean
post_mean = a1_hat / (a1_hat + a2_hat)
print("Posterior Mean (Analytic):", post_mean)

# Plot the analytic posterior
fig = plt.figure(figsize=(10,4))
ax = fig.add_subplot(111)
X = np.linspace(0,1, 1000)
ax.plot(X, stats.beta(a1_hat, a2_hat).pdf(X), "r")

# Plot the prior
ax.plot(X, stats.beta(a1, a2).pdf(X), "g")

# Cleanup
ax.set(title="Posterior Distribution (Analytic)", ylim=(0,12))
ax.legend(["Posterior (Analytic)", "Prior"])

# Metropolis-Hastings (metropolis hastings) using Markov chains 
print("Timing: 1 loops, best of 3: 356 ms per loop")

# Metropolis-Hastings parameters
G1 = 1000 # burn-in period
G = 10000 # draws from the (converged) posterior

# Model parameters
sigma = 0.1
thetas = [0.5] # initial value for theta
etas = np.random.normal(0, sigma, G1+G) # random walk errors
unif = np.random.uniform(size=G1+G) # comparators for accept_probs

# Callable functions for likelihood and prior
prior_const = gamma(a1) * gamma(a2) / gamma(a1 + a2)
mh_ll = lambda theta: _likelihood(theta, nobs, Y.sum())

def mh_prior(theta):
    """
    Prior distribution for Metropolis-Hastings algorithm for a theta.
    """
    prior = 0
    if theta >= 0 and theta <= 1:
        prior = prior_const*(theta**(a1-1))*((1-theta)**(a2-1))
    return prior

mh_accept = lambda theta: mh_ll(theta) * mh_prior(theta)

theta_prob = mh_accept(thetas[-1])

# Metropolis-Hastings iterations
for i in range(G1+G):
    # Draw theta
    # Generate the proposal
    theta = thetas[-1]
    theta_star = theta + etas[i]
    theta_star_prob = mh_accept(theta_star)
    # Calculate the acceptance probability
    accept_prob = theta_star_prob / theta_prob
    # Append the new draw
    if accept_prob > unif[i]:
        theta = theta_star
        theta_prob = theta_star_prob
    thetas.append(theta)

# Posterior Mean
print("Posterior Mean (MH):", np.mean(thetas[G1:]))

# Plot the posterior
fig = plt.figure(figsize=(10,4))
ax = fig.add_subplot(111)

# Plot MH draws
ax.hist(thetas[G1:], bins=50, normed=True)

# Plot analytic posterior
X = np.linspace(0,1, 1000)
ax.plot(X, stats.beta(a1_hat, a2_hat).pdf(X), "r")

# Plot prior
ax.plot(X, stats.beta(a1, a2).pdf(X), "g")

# Cleanup
ax.set(title="Metropolis-Hastings via pure Python (10,000 Draws; 1,000 Burned)", ylim=(0,12))
ax.legend(["Posterior (Analytic)", "Prior", "Posterior Draws (MH)"])

# Metropolis-Hastings in Cython
cdef double likelihood(double theta, int T, int s):
    """
    Calculate Metropolis-Hastings distribution samples using Cython functions.
    """
    return pow(theta, s)*pow(1-theta, T-s)

cdef double prior(double theta, double a1, double a2, double prior_const):
    """
    Double of the prior distribution.
    """
    if theta < 0 or theta > 1:
        return 0
    return prior_const*pow(theta, a1-1)*pow(1-theta, a2-1)

cdef np.ndarray[np.float64_t, ndim=1] draw_posterior(np.ndarray[np.float64_t, ndim=1] theta, double eta, double unif, int T, int s, double a1, double a2, double prior_const):
    cdef double theta_star, theta_star_prob, accept_prob
    theta_star = theta[0] + eta
    theta_star_prob = likelihood(theta_star, T, s) * prior(theta_star, a1, a2, prior_const)
    accept_prob = theta_star_prob / theta[1]
    if accept_prob > unif:
        theta[0] = theta_star
        theta[1] = theta_star_prob
    return theta

def mh(double theta_init, int T, int s, double sigma, double a1, double a2, int G1, int G):
    """
    Metropolis-Hastings algorithm using Cython.
    """ 
    cdef np.ndarray[np.float64_t, ndim = 1] theta, thetas, etas, unif
    cdef double prior_const, theta_prob
    cdef int t
    prior_const = gamma(a1) * gamma(a2) / gamma(a1 + a2)
    theta_prob = likelihood(theta_init, T, s) * prior(theta_init, a1, a2, prior_const)
    theta = np.array([theta_init, theta_prob])
    thetas = np.zeros((G1+G,))
    etas = np.random.normal(0, sigma, G1+G)
    unif = np.random.uniform(size=G1+G)
    for t in range(G1+G):
        theta = draw_posterior(theta, etas[t], unif[t], T, s, a1, a2, prior_const)
        thetas[t] = theta[0]
    return thetas

print("Timing: 10 loops, best of 3: 20.7 ms per loop")
thetas = mh(0.5, nobs, Y.sum(), sigma, a1, a2, G1, G)
