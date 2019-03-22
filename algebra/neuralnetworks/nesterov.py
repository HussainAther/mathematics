import numpy as np

"""
Nesterov's method for proximal gradient descent.
"""

def grad(f, x, deltax):
    """
    Compute the gradient numerically using our function f that takes in x as a variable.
    """
    xval = f(x) # evaluate the function f at x.
