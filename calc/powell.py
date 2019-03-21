import numpy as numpy

"""
Powell's algorithm for finding local minima.
"""
def gaussElim(a, b):
    """
    Compute linear solution of matrices a and b.
    """

def p(x):
    """
    For a series of values x, find local minima using the Powell method.
    """
    lam = 100 # to normalize the penalty on a scale of 100
    c = 2*np.sqrt(2) # pull this out in front for simplifying the polynomial
    A = np.array([[c*x[1] + x[2], -x[2], x[2]], [-x[2], x[2], -x[2]], [x[2], -x[2],  c*x[0] + x[2]]])/c]) # polynomials
    b = np.array([0, -1, 0])
    v = gaussElim(A, b) # perform Gaussian elimination to find a linear solution
    weight = x[0] + x[1] + np.sqrt(2)*x[2] # weight used for our solution
    penalty = max(0, abs(v[1]) - 1)**2 + max(0, -x[0])**2, max(0, -x[1])**2 + max(0, -x[2)**2
    return weight+penalty*lam

