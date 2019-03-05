import numpy as np

"""
Laguerre's polynomials are solutison to the second-order differential equation

xy'' + (1 - x)y' + ny = 0

or soutions of

xy'' + (alpha + 1 - x)y' + ny = 0

They arise in radial parts of solutions to the Schrödinger equation for a one-electron atom.
They describe static Wigner functions of oscillator systems in quantum mechanics in phase space.
"""

lp = { # Laguerre polynomials
    0: 1,
    1: -x + 1,
    2: (-1/2)*(x-4* x +2),
    3: (1/6)*(-x**3 + 9*x**3 - 18*x + 6),
    4: (1/24)*(-x**4 - 16*x**3 + 72*x**2 - 96*x + 24),
    5: (1/120)*(-x**5 + 25*x**4 - 200*x**3 - 96*x + 24),
    6: (1/720)*(x**6 -36*x**5 + 450*x**4 - 2400*x**3 + 5400*x**2 - 4320*x + 720)
}

def laguerre(x, k):
    """
    Return up to kth order Laguerre polynomials
    """
    results = [] # the first two polynomials are by definition
    if k == 0:
        return [1]
    if k == 1:
        return [1, 1-x]
    else:
        for i in range(2, k+1):
            results.append(((2 + 1 - x) * lp(i) - i*lp(i-1) / (i+1))) # calculate the polynomial using the recurrence relation
    return results


