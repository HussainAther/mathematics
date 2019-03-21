import numpy as numpy

"""
Powell's algorithm for finding local minima.
"""

def p(x):
    """
    For a series of values x, find local minima using the Powell method.
    """
    lam = 100 # to normalize the penalty on a scale of 100
