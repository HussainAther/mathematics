import numpy as np

"""
Minorization-maximization.
"""

def mle(pmat, max_iter=100):
    n = pmat.shape[0]
    wins = np.sum(pmat, axis=0)
