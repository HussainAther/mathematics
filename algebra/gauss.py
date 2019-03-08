import numpy as np

def gj(a, n)
    """
    Gaussian-Jordan elimination on two input matrices represented by a and b.
    """
    n = np.size(a,0)
    indxc = [0]*n # bookkeeping during pvots
    ipiv = [0]*n
    indxr = [0]*n
    for j in range(0, n): # main loop over columns that we reduce
        ipiv[j] = 0
    for i in range(0, n):
        big = 0,0
        for j in range(0, n):
            if ipiv[j] != 1:
                for k in range(0, n):
                    if ipiv[k] == 0:
                        if abs(a[j][k] >= big):
                            big = abs(a[j][k])
                            irow = j
                            icol = k
        ipiv[icol] += 1


