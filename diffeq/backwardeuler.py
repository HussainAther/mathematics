import math
import matplotlib.pyplot as plt
import numpy as np

"""
We use the Backward (backward) Euler (euler) method for evaluating differential equations.
"""

def feval(funcName, *args):
    return eval(funcName)(*args)

def be(f, y0, x_vals, h):
    """
    Compute the Backawrd Euler method for a function f with list initial differential equations y0,
    over values x_vals, with step size h.
    """
    n = len(y0) # number of ordinary differential equations
    sub = int((x_vals[-1] - x_vals[0]))/h) # number of intervals
    x = x_vals[0] # Initialize x value.
    y = y0 # Initialize y values.
    xreturn = [x] # x results list
    yreturn = [y[0]] # y results list
    for i in range(sub):
        yprime = feval(f, x+h, y)
        yp = [0]*len(yprime) # used as the product with yprime
        for j in range(len(yprime)):
            yp[i] = yprime[i]*(1/(1+h)) # Normalize each value using our stepsize as a product with yprime.
        for j in range(n): # Backward Euler method
            y[j] += h*yp[j] # Run our step size on the yp product.
        x += h
        xreturn.append(x)
        for r in range(len(y)):
            yreturn.append(y[r]) # Use numpy's append.
    return [xreturn, yreturn]
