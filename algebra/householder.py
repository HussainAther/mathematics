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

    # Nested list comprehension to calculate matrix multiplication
    return [[sum(el_m * el_n for el_m, el_n in zip(row_m, col_n)) for col_n in tuple_N] for row_m in M]

def trans_matrix(M):
    """Take the transpose of a matrix."""
    n = len(M)
    return [[ M[i][j] for i in range(n)] for j in range(n)]

def norm(x):
    """Return the Euclidean norm of the vector x."""
    return sqrt(sum([x_i**2 for x_i in x]))

def Q_i(Q_min, i, j, k):
    """Construct the Q_t matrix by left-top padding the matrix Q
    with elements from the identity matrix."""
    if i < k or j < k:
        return float(i == j)
    else:
        return Q_min[i-k][j-k]

def householder(A):
    """Performs a Householder Reflections based QR Decomposition of the
    matrix A. The function returns Q, an orthogonal matrix and R, an
    upper triangular matrix such that A = QR."""
    n = len(A)

    # Set R equal to A, and create Q as a zero matrix of the same size
    R = A
    Q = [[0.0] * n for i in xrange(n)]

    # The Householder method
    for k in range(n-1):
        # Create identity matrix of same size as A
        I = [[float(i == j) for i in xrange(n)] for j in xrange(n)]
