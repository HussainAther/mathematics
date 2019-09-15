import numpy as np
import random

from scipy import stats

def calcdist(x1, x2, sigma):
    """
    Calculate the distance between x1 and x2 using the DANN metric at
    query locus.   
    """
    diff = x1 - x2
    dist = diff.T.dot(sigma).dot(diff)
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
    nXmean = nX.mean(axis=0)
    ny = y[nn]
    nclasses = np.unque(ny) # neighborhood classes
    classfreq = {} # class frequencies
    withinclasscov = np.zeros((nfeatures, nfeatures)) # covariance matrices
    betweenclasscov = np.zeros((nfeatures, nfeatures))
    for class in nclasses:
        classindices = np.where(ny == class)[0] # class indices
        classfreq[class] = np.sum(ny == class) / nsize
        classcov = np.cov(nX[classindices, :], rowvar=False) # class covariance
        withinclasscov += classcov * classfreq[class]
        classmean = nX[classindices, :].mean(axis=0)
        betweenclasscov += np.outer(classmean - nXmean, classmean - nXmean) * classfreq[class] 
    Wstar = np.linalg.pinv(np.nan_to_num(np.power(withinclasscov, .5)))
    Bstar = np.dot(Wstar, betweenclasscov).dot(Wstar)
    I = np.identity(nfeatures)
    sigma = Wstar.dot(Bstar + epsilon * I).dot(Wstar)
    dists = []
    for row in X:
        dists.append(calcdist(x, row, sigma))
    dists = np.array(dists)
    nearest = dists.argsort()[:k]
    prediction = stats.mode(y[nearest]).mode[0]
    return prediction
