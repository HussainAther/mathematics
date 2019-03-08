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
    n = len(np.size(a,0)) # matrix size
    vv = [0]*n # implicit scaling of each row
    lu = a
    big = 0
    temp = 0
    TINY = 1e-40
    d = 1
    for i in range(0, n):
        big = 0
        for j in range(0, n):
            if ((temp=abs(lu[i][j])) > big):
                big = temp
        if big == 0:
            print("Singular matrix in LU decomposition")
            return
    for k in range(0, n):
        big = 0
        for i in range(k, n):
            temp = vv[i]*abs(lu[i][k])
            if temp > big:
                big = temp
                imax = i
        if k != imax:
            for j in range(0, n):
                temp = lu[imax][j]
                lu[imax][j] = lu[k][j]
                lu[k][j] = temp
            d = -d
            vv[imax] = vv[k]
        indx[k] = imax
        if lu[k][k] == 0:
            lu[k][k] = TINY
        for i in range(k+1,n):
            temp = lu[i][k] /= lu[k][k] # divide by pivot element
            for j in range(k+1, n): # reduce remaining submatrix
                lu[i][j] -= temp*lu[k][j]
    return lu

