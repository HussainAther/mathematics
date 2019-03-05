import numpy as np
import matplotlib.pyplot as plt

"""
Jacobi's method is a way of computing eigenvalues and eigenvectors of a real symmetric matrix.
"""

def Jacobi(a, i, j, ip, iq):
    """
    Compute all eigenvalues and eigenvectors of a real symmetric matrix a of side-length n and output
    d[0...n-1] that has the eigenvalues of a sorted into descending order while v[0...n-1][0...n-1] is a
    matrix whose columns contain the corresponding nromalized eigenvectors. nrot contains
    """

