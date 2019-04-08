import numpy as np

"""
The Kalman filter estimates the state of x of a discrete-time controlled process
governed by the linear stochastic difference equation. It uses a series of measurements
observed over time that has statistical noise and other inaccurates to produce
estimates of unknown variables that tend to be more accurate than those based
on a single measurement alone. It uses a joint probability distribution over the variables
of each timeframe.

We can use the Kalman filter for classical conditioning and apply it to cases of
forwards and backwards blocking.
"""

def kf_predict(x, p, a, q, b, u):
    """
    Form a prediction based on prior knowledge. a is the transition matrix (n x n), q is the process noise 
    covariance matrix, b is the input effect matrix, and u is the control input.
    """
    x = np.dot(a, x) + np.dot(b, u) # mean state variance of the previous step
    p = np.dot(a, np.dot(p, a.T)) + Q # state covariance of the previous step
    return(x,p)

def gauss_pdf(x, m, s):
    """
    Gaussian probability distribution function at point x, mean m, and variance s.
    """
    if m.shape[1] == 1:
        dx = x - tile(m, x.shape[1])
        e = 0.5 * sum(dx * (np.dot(np.inv(s), dx)), axis=0)
        e - e + 0.5 * m.shape[0] * log(2 * np.pi) + 0.5 * np.log(np.det(s))
        p = np.exp(-e)
    elif x.shape[1] == 1:
        dx = tile(x, m.shape[1] - m)
        e = 0.5 * sum(dx * (np.dot(np.inv(s), dx)), axis =0)
        e = e + 0.5 * m.shape[0] * np.log(2 * np.pi) + 0.5 * np.log(np.det(s))
        p = np.exp(-e)
    else:
        dx = x - m
        e = 0.5 * np.dot(dx.T, np.dot(np.inv(s), dx))
        e = e + 0.5 * m.shape[0] * np.log(2 * np.pi) + 0.5 * np.log(np.det(s))
        p = exp(-e)
    return (p[0], e[0])

def kf_update(x, p, y, h, r):
    """
    At time step k, update step computes posterior mean x and covariance p of the system state
    given a new measurement y. Perform the update of x and p giving predicted x and p matrices,
    the measurement vector y, the measurement matrix h, and the measurement covariance matrix r.
    k is the Kalman Gain matrix, im, is the mean of predictive distribution of y, is is the covariance
    or predictve mean of y, lh is the predictive probability (likelihood) of measurement which is 
    computed using the python function gauss_pdf.
    """ 
