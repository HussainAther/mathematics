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

def logr(minn, maxn, f):
    """
    Return and array of values distributed as log(values), an evenly spaced array
    of values between log(minn) and log(maxn). f is the factor of space between values.
    """
    maxi = int(np.floor(np.log(1*maxn/minn) / np.log(f)))
    return np.array([minn * (f**i) for i in range(maxi+1)])

def gp(a, d, tau):
    """
    Estimate correlation dimension of a set of points for an array a in d-dimensional space with tau time delay.
    Return correlations and slope.
    """
    sd = np.std(a) # standard deviation
    o = embed(a, d, tau)
    n = len(o)
    r = logr(.1*sd, .7*sd, 1.03) 
    dists = np.zeros(shape=(n,n)) # initialize distance matrix
    rbase = np.zeros(shape=(n,n)) # base matrix
    for i in range(n):
        for j in range(i, n):
            dists[i][j] = np.linalg.norm(o[i] - o[j])
            rbase[i][j] = 1
    C = [] # correlation dimension values
    for i in r: # logarithmic values
        rmat = rbase * i # rmat is our matrix of log values for each iteration
        hv = np.heaviside(rmat-dists, 0) # Heaviside step function
        corr = (2/float(n*(n-1)))*np.sum(hv)
        C.append(corr) # append the corrleation value
    """
    We may make a strong assumption that the log-log plot is a smooth monotonic function
    such that the slope in the scaling region should be the maximum gradient
    """
    grads = np.gradient(np.log2(C), np.log2(r)).sort()
    D = np.mean(grads[-5:]) # slope in the scaling region is the mean of the final five maximum gradients
    return C, D

