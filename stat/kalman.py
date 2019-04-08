import numpy as np

"""
The Kalman filter estimates the state of x of a discrete-time controlled process
governed by the linear stochastic difference equation. It uses a series of measurements
observed over time that has statistical noise and other inaccurates to produce
estimates of unknown variables that tend to be more accurate than those based
on a single measurement alone. It uses a joint probability distribution over the variables
of each timeframe.
"""

def kf_predict(x, p, a, q, b, u):
    """
    Form a prediction based on prior knowledge.
    """
    x = np.dot(a, x) + np.dot(b, u) # mean state variance of the previous step
    p = np.dot(a, np.dot(p, a.T)) + Q # state covariance of the previous step
    return(x,p) 
