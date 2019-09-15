import numpy as np

from scipy.signal import argrelextrema

"""
For polynomials of the form
g(X) = a0 + a^TX + X^TAX
"""

def localmax(a):
    """
    For a list a, return True if there is a local maximum/a.
    """
    if argrelextrema(a, np.greater):
        return True
    return False

def poly(a0, a, X, A):
    """
    For some matrix X, return the second-order polynomial 
    histogram estimator. AX = ax
    """
    return a0 + np.multiply(np.transpose(a), X) + np.multiply(np.transpose(X), A*X)
 
def sophe(data, interval, threshold, v):
    """
    SOPHE Second-order polynomial histogram estimators for list of data, interval
    for which the data has been scaled, threshold value for cutting off data, binwidth v.
    """
    bins = []
    tempbin = []
    for i in data:
        tempbin.append(i)
        if len(tempbin) == v:
            tempbin.append(i)
            bins.append(tempbin)            
            tempbin = []
    obs = [] # observations
    for i in bins:
        if sum(i)/len(i) >= threshold:
            obs.append(i)
    functions = [] # function for each bin
    modalbins = []
    for i in obs:   
        a0 = 0
        a = np.cov(i)
        A = 5
        if localmax(poly(a0, a, i, A)): # if there is a local maxima in the polynomial, there is a mode
            modalbins.append(1)
        else:
            modalbins.append(0)
   
