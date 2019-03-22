import numpy as np

"""
Nesterov's method for proximal gradient descent.
"""

def grad(f, x, deltax):
    """
    Compute the gradient numerically using our function f that takes in x as a variable.
    """
    xval = f(x) # evaluate the function f at x.
    step = f(x + deltax) # step forward with deltax
    return (step - xval) / deltax # return the difference over the deltax value

def nes(f, L, dim, xinit=None):
    """
    Use the Nesterov method for proximal gradient descent. We improve convergence
    and can add a momentum term such that we relax the descent property. We update our
    function with a momenutm value that accounts ofr hte step size.
    """
