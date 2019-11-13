import numpy as np

from convergence import trapezoidal

"""
Adaptive integration lets us iterate over an integral nd compare the 
results produced by n and 2n intervals. If the difference is smaller
than some tolerance epsilon, then the value of 2n is returned. Otherwise,
cut n in half and repeat the iteration.
"""

def midpoint(f, a, b, n):
    """
    Midpoint integration.
    """
    h = float(b-a)/n
    result = 0
    for i in range(n):
        result += f((a + h/2.0) + i*h)
    result *= h
    return result

def adaint(f, a, b, eps, method="midpoint"):
    """
    For function f over interval  to be and tolerance eps, use the midpoint
    integration method for adaptive integration.
    """
    nlimit = 100000 # some really big number that we can start with
    n = 2
