from math import sqrt,exp
from numpy import empty
from random import random,randrange
from visual import sphere,curve,display

"""
Simpler functions
"""

N = 25
R = 0.02
Tmax = 10.0
Tmin = 1e-3
tau = 1e4

# Function to calculate the magnitude of a vector
def mag(x):
    return sqrt(x[0]**2+x[1]**2)
