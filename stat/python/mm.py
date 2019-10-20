import numpy as np

"""
Minorization-maximization reparametrized Bradley-Terry parameters 
into a convex function. The maximum-likelihood parameters can be 
found with convex optimization methods.
"""

def mle(pmat, max_iter=100):
    """
    Maximum-likelihood estimation using pairwise probabilities.
    """
    n = pmat.shape[0]
    wins = np.sum(pmat, axis=0)
    params = np.ones(n, dtype=float)
    for _ in range(max_iter):
        tiled = np.tile(params, (n, 1))
        combined = 1.0 / (tiled + tiled.T)
        np.fill_diagonal(combined, 0)
        nxt = wins / np.sum(combined, axis=0)
        nxt = nxt / np.mean(nxt)
        if np.linalg.norm(nxt - params, ord=np.inf) < 1e-6:
            return nxt
        params = nxt


