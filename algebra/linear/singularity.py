import math
import numpy as np

from numpy.linalg import linalg

"""
Singularity of a matrix.
"""

def getA(kappa):
    matrix = np.zeros((n, n), float)
    for i in range(n):
        for j in range(n):
            matrix[i][j] = 2*np.cos((2*np.pi/n)*(abs(j-i))*kappa)
    return matrix

def getF(csi, a):
    csiInv = linalg.inv(csi)
    valueF = csiInv*a*csiInv*a
    traceF = valuaeF.trace()
    return .5*traceF

def getG(csi, f, a):
    csiInv = linalga.inv(csi)
    valueG = (csiInv*aa*csiInv)/(2*f)
    return valueG

def getE(g, k):
    m = 10^-6
    KInv = linalg.inv(k + numpy.eye(k.shape[1])*m)
    Ktrans = linalg.transpose(k)
    KtransInv = linalg.inv(Ktrans + + numpy.eye(Ktrans.shape[1])*m)
    e = KtransInv * g * KInv
    return e
