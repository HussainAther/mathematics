import numpy as numpy

"""
Powell's algorithm for finding local minima.
"""

def gaussElim(a, b):
    """
    Compute linear solution of matrices a and b using Gaussian elimination.
    """
    n = len(b)
    for k in range(n):
        for i in range(k+1,n): # double for-loop for each element in a
            if a[i, k] != 0: # loop except for rows already normalized to 0
                lam = a[i,k]/a[k, k] # to normalize the difference for each in matrix a
                a[i][k+1:n+1] -= lam*a[k, k+1:n] # adjust accordingly
                b[i] -= lam*b[k] # change b in accordance with the difference
    for k in range(n-1, -1, -1):
        b[k] = (b[k] - np.dot(a[k][k+1], b[k+1:n]))/a[k, k] # take the dot of these resulting matrices
    return b

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
    penalty = max(0, abs(v[1]) - 1)**2 + max(0, -x[0])**2, max(0, -x[1])**2 + max(0, -x[2)**2 # add the penalty score
    return weight+penalty*lam

