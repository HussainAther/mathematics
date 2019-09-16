import numpy as np 
    
from scipy.spatial.distance import cdist

def sammon(x, n, display = 2, inputdist = "raw", maxhalves = 20, maxiter = 500, tolfun = 1e-9, init = "default"): 
    """
    Sammon mapping on a dataset x. Use the nonlinear mapping procedure on 
    multivariate data with rows of patterns and columns of features. 
    maxiter maximum number of iterations, tolfun relative tolerance for the objective
    function, maxhalves max number of step halvings, input can be "distance" to 
    use pairwise distances as input, display can be 0 to 2 for verbosity, 
    init is "pca" for raw input, "cmdscale" for distances, or can be "random"
    or "default".
    """
    if inputdist == "distance":
        D = x
        if init == "default":
            init = "cmdscale"
    else:
        D = cdist(x, x)
        if init == "default":
            init = "pca" 
