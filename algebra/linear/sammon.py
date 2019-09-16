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
    for i in range(maxiter):
        # Compute gradient, Hessian and search direction (note it is actually
        # 1/4 of the gradient and Hessian, but the step size is just the ratio
        # of the gradient and the diagonal of the Hessian so it doesn't
        # matter).
        delta = dinv - Dinv
        deltaone = np.dot(delta,one)
        g = np.dot(delta,y) - (y * deltaone)
        dinv3 = dinv ** 3
        y2 = y ** 2
        H = np.dot(dinv3,y2) - deltaone - np.dot(2,y) * np.dot(dinv3,y) + y2 * np.dot(dinv3,one)
        s = -g.flatten(order='F') / np.abs(H.flatten(order='F'))
        y_old = y
        # Use step-halving procedure to ensure progress is made
        for j in range(maxhalves):
            s_reshape = np.reshape(s, (-1,n),order='F')
            y = y_old + s_reshape
            d = cdist(y, y) + np.eye(N)
            dinv = 1 / d
            delta = D - d
            E_new = ((delta**2)*Dinv).sum()
            if E_new < E:
                break
            else:
                s = 0.5*s 
