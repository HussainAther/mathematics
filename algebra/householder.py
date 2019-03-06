import numpy as np

"""
Householder algorithm reduces an n x n matrix A to tridiagonal form by n - 2 orthogonal transformations.
Each transformation annihilates the required part of a whole column and whole corresponding row.
The Householder matrix P has the form:

P = 1 - 2w dot w^T

in which w is a real vector with |w|^2 = 1.
"""

def mult_matrix(M, N):
    """Multiply square matrices of same dimension M and N"""
    tuple_N = zip(*N)
    
