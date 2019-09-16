import numpy as np 
    
from scipy.spatial.distance import cdist
from cmdscale import cmdscale

def cmdscale(D):
    """
    Classical multidimensional scaling (MDS) for symmetric distance matrix D.
    """
    # Number of points                                                                        
    n = len(D)
    # Centering matrix                                                                        
    H = np.eye(n) - np.ones((n, n))/n
    # YY^T                                                                                    
    B = -H.dot(D**2).dot(H)/2
    # Diagonalize                                                                             
    evals, evecs = np.linalg.eigh(B)
    # Sort by eigenvalue in descending order                                                  
    idx   = np.argsort(evals)[::-1]
    evals = evals[idx]
    evecs = evecs[:,idx]
    # Compute the coordinates using positive-eigenvalued components only                      
    w, = np.where(evals > 0)
    L  = np.diag(np.sqrt(evals[w]))
    V  = evecs[:,w]
    Y  = V.dot(L)
    return Y, evals[evals > 0]

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
    N = x.shape[0]
    scale = 0.5 / D.sum()
    D = D + np.eye(N)     
    Dinv = 1 / D
    if init == "pca":
        [UU,DD,_] = np.linalg.svd(x)
        y = UU[:,:n]*DD[:n] 
    elif init == "cmdscale":
        y,e = cmdscale(D)
        y = y[:,:n]
    else:
        y = np.random.normal(0.0,1.0,[N,n])
    one = np.ones([N,n])
    d = cdist(y,y) + np.eye(N)
    dinv = 1. / d
    delta = D-d 
    E = ((delta**2)*Dinv).sum()  
