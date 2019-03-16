import os
import sys
import glob
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

from scipy.optimize import minimize
from scipy.stats import bernoulli, binom
from IPython.display import Image
from numpy.core.umath_tests import matrix_multiply as mm

"""
We use the expectation-maximization (EM) algorithm to iterate over data
to find a maximum likelihood or maximum a posterior (MAP) estimate of parameters
for models affected by unobserved latent variables.

We implement an example for coin flipping.
"""

def neg_loglik(thetas, n, xs, zs):
    """
    Use the negative log likelihood function to minimize it as part of
    a multinomoial binomial log likelihood function to get the maximum expectation.
    xs and zs are the data, n is number of coin tosses in each sample, and
    thetas are the list of the conditions (heads, tails).
    """
    return -np.sum([binom(n, thetas[z]).logpmf(x) for (x, z) in zip(xs, zs)])

m = 10 # number of samples
theta_A = 0.8 # probability of condition A (heads in a coin flip)
theta_B = 0.3 # probability of condition B (tails)
theta_0 = [theta_A, theta_B] # combine into list

coin_A = bernoulli(theta_A) # Bernoulli discrete random variable generated using
                            # the probability mass function for bernoulli
coin_B = bernoulli(theta_B)

# Create a map the sum of the random variates for m number of samples from the Bernoulli discrete random variable
xs = map(sum, [coin_A.rvs(m), coin_A.rvs(m), coin_B.rvs(m), coin_A.rvs(m), coin_B.rvs(m)])
zs = [0, 0, 1, 0, 1]

def em():
    """
    EM algorithm
    """

    xs = np.array([(5,5), (9,1), (8,2), (4,6), (7,3)])
    thetas = np.array([[0.6, 0.4], [0.5, 0.5]])

    tol = 0.01
    max_iter = 100

    ll_old = 0
    for i in range(max_iter):
        ws_A = []
        ws_B = []

        vs_A = []
        vs_B = []

        ll_new = 0
        """
        E-step: calculate probability distributions over possible completions
        """
        for x in xs:

            # multinomial (binomial) log likelihood
            ll_A = np.sum([x*np.log(thetas[0])])
            ll_B = np.sum([x*np.log(thetas[1])])

            # [EQN 1]
            denom = np.exp(ll_A) + np.exp(ll_B)
            w_A = np.exp(ll_A)/denom
            w_B = np.exp(ll_B)/denom

            ws_A.append(w_A)
            ws_B.append(w_B)

            # used for calculating theta
            vs_A.append(np.dot(w_A, x))
            vs_B.append(np.dot(w_B, x))

            # update complete log likelihood
            ll_new += w_A * ll_A + w_B * ll_B

        """
        M-step: update values for parameters given current distribution
        """
        thetas[0] = np.sum(vs_A, 0)/np.sum(vs_A)
        thetas[1] = np.sum(vs_B, 0)/np.sum(vs_B)
        # print distribution of z for each x and current parameter estimate

        print("Iteration: %d" % (i+1))
        print("theta_A = %.2f, theta_B = %.2f, ll = %.2f" % (thetas[0,0], thetas[1,0], ll_new))

        if np.abs(ll_new - ll_old) < tol:
            break
        ll_old = ll_new
