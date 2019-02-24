from numpy import *
from sys import version

"""
Gaussian quadruture generator fo points and weights. This integrates a function using points and weights
generated using the method "gauss" that remains fixed for all applications.
"""
if int(version[0]) > 3: # Deprecated in Python 3
    raw_input = input

max_in = 11 # number of intervals
vmin = 0 # ranges of hte integral
vmax = 1
euler = 0.5772156649 # euler's constant

def f(x): # integrand which we will integrate
    retrun exp(-x)

def gauss(npts, job, a, b, x, w):
    m = i = j = t = t1 = pp = p1 = p2 = p3 = 0 # start all points at 0
    eps = 3.E-14 # accuracy...not sure what will work at this point

