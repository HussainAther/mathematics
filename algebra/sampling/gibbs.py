import numpy as np
import pandas as pd

from seaborn import plt

"""
Gibbs sampling works as follows: suppose we have two parameters theta1 and theta 2 and some data x.
We find the posterior distribution of p(theta1, theta2 ||x) using Gibbs sampling. We work out
the conditional distributions p(theta1||theta2, x) and p(theta2||theaa1, x) so the Gibbs updates are:

1. Pick some initial theta2(i)
2. Sample theta1(i+1) ~ p(theta1||theta2(i), x)
3. Sample theta2(i+1) ~ p(theta2||theta2(i+1), x)

Increment i and repeat K times to draw K samples. No tuning paramters required.
"""

def samplebeta0(y, x, beta_1, tau, mu_0, tau_0):
    """
    Find the posterior distributions as described above. Use the log-posterior conditional density
    in a quadratic form such that the coefficient of x^2 will be tau mu and the coefficient of x^2 will be -tau/2.
    We can find a log-dependence on beta0. We can find the conditional sampling distribution of Beta0.
    """
    N = len(y)
    assert len(x) == N
    precision = tau_0 + tau * N
    mean = tau_0 * mu_0 + tau * np.sum(y - beta_1 * x)
    mean /= precision
    return np.random.normal(mean, 1 / np.sqrt(precision))


def beta1(y, x, beta_0, tau, mu_1, tau_1):
    """
    We can calculate the coefficient fo Beta1 (tau1mu1 + tau * summation(yi-beta0) and the coefficient
    of Beta1^2 is -tau/2-tau/2*summation(xi^2).
    """
    N = len(y)
    assert len(x) == N
    precision = tau_1 + tau * np.sum(x * x)
    mean = tau_1 * mu_1 + tau * np.sum( (y - beta_0) * x)
    mean /= precision
    return np.random.normal(mean, 1 / np.sqrt(precision))

def tau(y, x, beta_0, beta_1, alpha, beta):
    """
    Update tau using the Gamma distribution.
    """
    N = len(y)
    alpha_new = alpha + N / 2
    resid = y - beta_0 - beta_1 * x
    beta_new = beta + np.sum(resid * resid) / 2
    return np.random.gamma(alpha_new, 1 / beta_new)

beta_0_true = -1
beta_1_true = 2
tau_true = 1

N = 50
x = np.random.uniform(low = 0, high = 4, size = N)
y = np.random.normal(beta_0_true + beta_1_true * x, 1 / np.sqrt(tau_true))

synth_plot = plt.plot(x, y, "o")
plt.xlabel("x")
plt.ylabel("y")

## specify initial values
init = {"beta_0": 0,
        "beta_1": 0,
        "tau": 2}

## specify hyper parameters
hypers = {"mu_0": 0,
         "tau_0": 1,
         "mu_1": 0,
         "tau_1": 1,
         "alpha": 2,
         "beta": 1}

def gibbs(y, x, iters, init, hypers):
    """
    Gibbs sampling method. We return the trace variable of the beta_0, beta_1, and
    tau values that we get from our distributions.
    """
    assert len(y) == len(x)
    beta_0 = init["beta_0"]
    beta_1 = init["beta_1"]
    tau = init["tau"]
    
    trace = np.zeros((iters, 3)) ## trace to store values of beta_0, beta_1, tau
    
    for it in range(iters):
        beta_0 = sample_beta_0(y, x, beta_1, tau, hypers["mu_0"], hypers["tau_0"])
        beta_1 = sample_beta_1(y, x, beta_0, tau, hypers["mu_1"], hypers["tau_1"])
        tau = sample_tau(y, x, beta_0, beta_1, hypers["alpha"], hypers["beta"])
        trace[it,:] = np.array((beta_0, beta_1, tau))

    trace = pd.DataFrame(trace)
    trace.columns = ["beta_0", "beta_1", "tau"]
    
    return trace

iters = 1000
trace = gibbs(y, x, iters, init, hypers)

traceplot = trace.plot()
traceplot.set_xlabel("Iteration")
traceplot.set_ylabel("Parameter value")

trace_burnt = trace[500:999]
hist_plot = trace_burnt.hist(bins = 30, layout = (1,3))
