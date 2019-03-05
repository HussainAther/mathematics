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
    3: (1/6)*(-x**3 + 9*x**3 - 18*x +6),
}
