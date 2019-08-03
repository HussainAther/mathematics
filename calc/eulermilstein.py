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
