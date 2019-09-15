import numpy as np

def sophe(data, interval, threshold, v):
    """
    SOPHE Second-order polynomial histogram estimators for list of data, interval
    for which the data has been scaled, threshold value, and v integer
    used as a scale in finding the binwidth.
    """
    binwidth = interval/v 
    obs = np.where(data >= threshold, data) # observations 
