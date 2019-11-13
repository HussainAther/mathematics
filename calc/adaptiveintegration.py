import numpy as np

from convergence import trapezoidal



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
