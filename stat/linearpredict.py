import numpy as np

"""
Linear prediction uses data points equally spaced along a line such that we use
values to autocorrelate and predict based on them.
"""

def memcof(a, m=5):
    """
    Takes a vector of list a. Return the mean square discrepancy as xms and m linear prediction coefficients
    as a list d.
    """
    p = 0
    n = len(a)
    wk1 = [0]*len(n)
