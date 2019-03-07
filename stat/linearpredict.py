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
    wk2 = [0]*len(n)
    wkm = [0]*len(m)
    for j in range(0, n):
        p += np.sqrt(a[j])
    xms = p/n
    wk1[0] = a[0]
    wk2[n-2] = a[n-1]
    
