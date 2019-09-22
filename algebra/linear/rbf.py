import numpy as np

def rbf(x, c, s):
    """
    Gaussian radial basis function (rbf) for neural networks. 
    """
    return np.exp(-1 / (2 * s**2) * (x-c)**2)
