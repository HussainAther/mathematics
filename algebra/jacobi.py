import numpy as np
import matplotlib.pyplot as plt

"""
Jacobi's method is a way of computing eigenvalues and eigenvectors of a real symmetric matrix.
"""
def eigsrt(d):
    """
    Given the eigenvalues d[0...n-1] and optionaly the eigenveectors v[0...n-1] as determined by Jacobi,
    this sorts the eigenvalues into descending order and rearranges the columns of v correspondingly.
    """
    n = len(d)
    for i in range(0, n):
        


def jacobi(a):
    """
    Compute all eigenvalues and eigenvectors of a real symmetric matrix a of side-length n and output
    d[0...n-1] that has the eigenvalues of a sorted into descending order while v[0...n-1][0...n-1] is a
    matrix whose columns contain the corresponding nromalized eigenvectors. nrot contains the Jacobi rotations
    that were required. Only the upper tirangle of a is accessed.
    """
    if np.size(a,0) != np.size(a,1):
        print("Error: matrix must be symmertic. E.g., of shape nxn")
        return
    n = np.size(a,0)
    v = np.matrix([0]*n,[0]*n)
    np.fill_diagonal(v, 1.0)
    b = np.diagonal(v) # b and d are diagonals that we initialize for convenience
    d = np.diagonal(v)
    z = np.zeros(n)
    for i in range(1,51):
        sm = 0 # sum the magnitude of off-diagonal elements
        for ip in range(0, n):
            for iq in range(ip+1, n+1):
                sm += abs(a[ip][iq])
        if sm == 0:
            eigsrt



