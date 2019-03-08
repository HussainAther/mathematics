import numpy as np

def gj(a, n)
    """
    Gaussian-Jordan elimination on two input matrices represented by a and b.
    """
    n = np.size(a,0)
    indxc = [0]*n
    ipiv = [0]*n
    indxr = [0]*n
    for j in range(0, n):

