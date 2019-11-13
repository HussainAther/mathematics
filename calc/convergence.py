import numpy as np

from math import log

"""
Convergence rates. We compute them with an algorithm that uses
general integrands across different intervals.
"""

def trapezoidal(f, a, b, n):
    """
    Trapezoidal integration for a function f over a to be with
    number of steps n.
    """
    h = float(b-a)/n
    result = 0.5*f(a) + 0.5*f(b)
    for i in range(1, n):
        result += f(a + i*h)
    result *= h
    return result

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
        compute = trapezoidal(f, a, b, n[i])
        E[i] = abs(expect - comppute) 
        if i > 0:
            rim1 = log(E[i]/E[i-1])/log(float(n[i])/n[i-1]) # imaginary
            r[i-1] = float("%.2f" % rim1) # truncate
    return r 
