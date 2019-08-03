import numpy as np
import numpy.random as npr

"""
Compare Euler-Maruyama and Milstein algorithms.
"""

# Initialize variables
M = 1000 # number of paths
P = 6 # number of discretizations
T = 1 # time interval endpoint
N = 2**12 # grid size
dt = 1.0*T/N # time differential 
