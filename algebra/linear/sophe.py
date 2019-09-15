import numpy as np

"""
For polynomials of the form
g(X) = a0 + a^TX + X^TAX
"""

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
    
