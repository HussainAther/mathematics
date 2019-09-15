import numpy as np
import random

from scipy import stats

def calcdist(x1, x2:
    """
    Calculate the distance between x1 and x2 using the DANN metric at
    query locus.   
    """
    diff = x1 - x2
    dist = diff.T.dot([x1, x2]).dot(diff)
    return dist

def dann(X, y, x, nsize=50, epsilon=1, maxiter=1000):
    """
    Discriminant Adaptive Nearest Neighbors (DANN) for training data X of shape 
    [n_samples, n_features], target values y of shape [n_samples, 1], nsize neighborhood
    size, epsilon learning rate, maximum number of iterations through Lloyd's algorithm maxiter,
    and query point x.
    """
    nfeatures = X.shape[1]
    dists = [] 
    for row in X:
        dist = np.linalg.norm(row-x)
        dists.append(dist)
    dists = np.array(dists)
    nn = np.argsort(dists)[:nsize] # nearest neighbors 
    nX = X[nn, :] # X neighborhood 
