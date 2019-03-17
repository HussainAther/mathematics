import urllib2
import numpy
from sklearn import datasets, linear_model
from math import sqrt
import matplotlib.pyplot as plot

"""

"""

def S(z, gamma):
    """
    Lasso coefficient shrinkage function used as a soft limiter such
    that, if the first input is larger than the second, the output is the
    first input reduced by the magnitude of the second.
    """
    if gamma >= abs(z):
        return 0.0
    return (z/abs(z))*(abs(z) - gamma)

