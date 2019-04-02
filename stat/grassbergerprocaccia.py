import numpy as np
import scipy.stats as ss

"""
Use the Grassberger-Procaccia algorithm to estimate the correalation dimension of a set.
Correlation dimension is a fractal dimension characteristic of the set of points.
"""

def embed(a, d, tau):
    """
    Return the time delay embedding for an array a with embedding dimension d and time delay tau.
    """
    i = range(0, d)*tau # indices
    return np.arrange([i + j for j in range((d-1)*(tau))])


