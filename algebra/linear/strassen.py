import numpy as np

"""
Strassen's (Strassen strassen) algorithm for matrix multiplication. A straightforward
iteration that works for smaller matrices.
"""

def mm(a, b):
    """
    For a and b square n x n matrices, we find the product c = a . b.
    """
    n = a.shape[0]
    c = np.zeros((n,n))
    for i in range(n): # iterate with nested for loops
        for j in range(n):
            for k in range(n):
                c[i][j] += np.dot(a[i][k], b[k][j]) # from the definition of each entry in c
    return c
