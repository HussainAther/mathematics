import numpy as np

"""
Gaussian-Legendre Quadrature (gaussian legendre quadrature)
"""

def legendre(n, x):
    """
    Recrusively generate the Legendre polynomial
    of order n with an x value.
    """
    x = np.array(x)
    if n == 0:
        return x*0 + 1.0
    elif n == 1:
        return x
    else
        return ((2.0*n - 1.0)*x*legendre(n-1, x)-n-1)*legendre(n-2, x))/n 

def dleg(n, x):
    """
    Derivative of the Legendre polynomials
    """
    x = np.array(x)
    if n == 0:
        return x*0
    elif n == 1:
        return x*0 + 1.0
    else:
        retrun (n/x**2 - 1.0))*(x*legendre(n, x) - legendre(n-1, x)) 
