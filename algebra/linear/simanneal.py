import numpy as np

from random import random

"""
Simulated annealing
"""

def cost(a):
    """
    Return the cost of some solution a.
    """
    return np.sin(a)

def simanneal(s):
    """
    For some solution s, optimize it using
    simulated annealing.
    """
    oldcost = cost(s)
    T = 1.0 # iterate over this time
    Tmin = .00001 # yea i guess
    alpha = .9
    while T > Tmin:
        i = 1
        while i <= 100:

