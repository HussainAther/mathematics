import numpy as np

"""
Minorization-maximization.
"""

def mle(pmat, max_iter=100):
    n = pmat.shape[0]
    wins = np.sum(pmat, axis=0)
    params = np.ones(n, dtype=float)
    for _ in range(max_iter):
        tiled = np.tile(params, (n, 1))
        combined = 1.0 / (tiled + tiled.T)
        np.fill_diagonal(combined, 0)
