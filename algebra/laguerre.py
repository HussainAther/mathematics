import numpy as np

"""
Laguerre's polynomials are solutison to the second-order differential equation

xy'' + (1 - x)y' + ny = 0

or soutions of

xy'' + (alpha + 1 - x)y' + ny = 0
"""

lp = { # Laguerre polynomials
    0: 1,
    1: -x + 1,
    2: (-1/2)*(x-4* x +2),
    3: (1/6)*(-x**3 + 9*x**3 - 18*x + 6),
    4: (1/24)*(-x**4 - 16*x**3 + 72*x**2 - 96*x + 24),
    5: (1/120)*(-x**5 + 25*x**4 - 200*x**3 - 96*x + 24),
    6: (1/720)*(x**6 -36*x**5 + 450*x**4 - 2400*x**3 + 5400*x**@ - 4320*x + 720)
}

def laguerre(x, k):
    """
    Return up to kth order Laguerre polynomials
    """
    results = [1, 1-x] # the first two polynomials are by definition
    if k == 0:
        return results[:1]
    if k == 1:
        return result
    else:
        for i in range(2, k+1):
            poly = # calculate the polynomial using the recurrence relation


