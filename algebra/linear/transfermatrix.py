import numpy as np

"""
Transfer matrix
"""

def transfermatrix(Pi):
    xlen, ylen = Pi.shape
    S = [0]*xlen
    for a in range(xlen):
        S[a] = 0
        for b in range(xlen):
            S[a] += P[b, a]*Pi[b]
    return S

