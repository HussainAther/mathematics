import numpy as np
from seaborn import plt
import pandas as pd

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
