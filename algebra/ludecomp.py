import numpy as numpy

"""
Lower-upper (LU) decomposition or factorization factors a matrix as the product of a lower triangular
matrix and an upper triangular matrix. The product sometimes includes a permutation matrix as well.
It can be viewed as the matrix form of Gaussian elimination.
"""

def ludecomp(a):
    """
    Given a matrix a, replace it iwth the LU decomposition of a rowwise permutation of itself.
    indx is an output vector that records the row permutation effected by the partial pivoting.
    d is output as +/- 1 depending on whether the number of row interchanges was even or add.
    """
    n = len(np.size(a,0))
    TINY = 1e-40
    d = 1
