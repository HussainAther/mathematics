import numpy as np
import random

from scipy import stats

def dann(X, y, nsize=50, epsilon=1, maxiter=1000):
    """
    Discriminant Adaptive Nearest Neighbors (DANN) for training data X of shape 
    [n_samples, n_features], target values y of shape [n_samples, 1], nsize neighborhood
    size, epsilon learning rate, maximum number of iterations through Lloyd's algorithm maxiter,

    """
    
