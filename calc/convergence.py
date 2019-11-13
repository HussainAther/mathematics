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
