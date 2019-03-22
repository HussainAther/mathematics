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

def nes(f, t, dim, xinit=None, eps=.05, ):
    """
    Use the Nesterov method for proximal gradient descent. We improve convergence
    and can add a momentum term such that we relax the descent property. We update our
    function with a momentum value that accounts for the step size.
    f is our function that we evaluate.
    t is our learning rate.
    dim is the number of dimensions of x.
    xinit is our initialized x value.
    eps (epsilon) is our tolerance used to stop the algorithm.
    """

    # lambda is the estimate sequence used to estimate the phi function used to
    # minimize our function f.
    lprev = 0 # previous lambda value
    lcurr = 1 # current lambda value

    
