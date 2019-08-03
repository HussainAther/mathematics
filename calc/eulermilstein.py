import numpy as np
import numpy.random as npr

"""
Compare Euler-Maruyama and Milstein algorithms.
"""

# Initialize variables.
M = 1000 # number of paths
P = 6 # number of discretizations
T = 1 # time interval endpoint
N = 2**12 # grid size
dt = 1.0*T/N # time differential 
lambda = 2.0
mu = 1.0
Xzero = 1.0

# Initialize functions.
def a(X): return lambda*X
def b(X): return mu*X
def bd(X): return mu*np.ones_like(X) 

# Brownian paths
dW = npr.normal(0.0, np.sqrt(dt), (M, N+1))
dW[:, 0] = 0.0
W = np.cumsum(dW, axis=1)

# Build the exact solutions at the ends.
ones = np.ones(M)
Xexact = Xzero*np.exp((lambda-.5*mu*mu)*ones+mu*W[:, -1])
Xemerr = np.empty((M, P))
Xmilerr = np.empty((M, P))
