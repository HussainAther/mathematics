import numpy as np

def rbf(x, c, s):
    """
    Radial basis function for neural networks. 
    """
    return np.exp(-1 / (2 * s**2) * (x-c)**2)
