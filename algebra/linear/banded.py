import numpy as np

"""
Solve a banded system of linear equaitons using Gaussian elimination and backsubstitution.

Return the vector solution to x = banded(A, v, up, down) and A.x = v in which v
is an array representing a vector of N elements that are eitehr real or complex. A
is an N by N banded matrix with "up" nonzero elements above the diagonal and "down" nonzero
elements below the diagonal. The matrix is specified as a 2-d array of (1+up+down) by N
elements with the diagonals of the original matrix along its rows.
"""


def banded(Aa,va,up,down):

    # Copy the inputs and determine the size of the system
    A = np.copy(Aa)
    v = np.copy(va)
    N = len(v)

    # Gaussian elimination
    for m in range(N):

        # Normalization factor
        div = A[up,m]

        # Update the vector first
        v[m] /= div
        for k in range(1,down+1):
            if m+k<N:
                v[m+k] -= A[up+k,m]*v[m]
