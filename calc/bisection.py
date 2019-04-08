from vpython import *
from vpython.graph import *

"""
Biscetion algorithm is a simple way for finding a zero of a function.
"""

eps = 1e-6 # precision
xminus = 0 # must contain zero
xplus = 7 # what we add to x as we determine the sign of the product
imax = 100 # number of iterations

def f(x):
    """
    Some function.
    """
    return 2*cos(x) -x

for i in range(0, imax):
    x = (xplus + xminus) / 2
    if f(xplus)*f(x) > 0: # the algorithm checks the product's sign of f with x and xplus
        xplus = x
    else:
        xminus = x
    if abs(f(x) < eps): # check for convergence
        print("The zero is at x=" + str(x))


