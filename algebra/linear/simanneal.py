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
