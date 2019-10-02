import math
import numpy as np

from numpy.linalg import linalg

"""
Singularity of a matrix.
"""

def getA(k):
    matrix = np.zeros((n, n), float)
    for i in range(n):
        for j in range(n):
            matrix[i][j] = 2*np.cos((2*np.pi/n)*(abs(j-i))*k)
    return matrix 
