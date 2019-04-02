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
    """
    sd = np.std(a) # standard deviation
    o = embed(a, d, tau)
    n = len(o)
    r = logr(.1*sd, .7*sd, 1.03) 
    dists = np.zeros(shape(n,n)) # initialize distance matrix
    rbase =  
