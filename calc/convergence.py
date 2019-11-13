import numpy as np

from math import log

"""
Convergence rates. We compute them with an algorithm that uses
general integrands across different intervals.
"""

def convrates(f, F, a, b, exps=14):
    """
    For two different functions f and F over interval from a to b as
    well as number of experiments exps, compute the rate of convergence. 
    """
    expect = F(b) - F(a) # expected rate
    n = np.zeros(exps, dtype=int)
    E = np.zeros(exps)
    r = np.zeros(exps-1)
    for i in range(exps):
        n[i] = 2**(i+1)
        computed = trapezoidal(f, a, b, n[i])
     
