import numpy as np 
    
from scipy.spatial.distance import cdist

def sammon(x, n, display = 2, inputdist = "raw", maxhalves = 20, maxiter = 500, tolfun = 1e-9, init = "default"): 
    """
    Sammon mapping on a dataset. Use the nonlinear mapping procedure on 
    multivariate data with rows of patterns and columns of features. 
    """
