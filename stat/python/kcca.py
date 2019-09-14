import numpy as np

def _listdot(d1, d2): 
    """
    Dot product for two lists.
    """
    return [np.dot(x[0].T, x[1]) for x in zip(d1, d2)]

def _listcorr(a):
    """
    Return pairwise row correlations for all items in array as a 
    list of matrices.
    """
    corrs = np.zeros((a[0].shape[1], len(a), len(a)))
    for i in range(len(a)):
        for j in range(len(a)):
            if j > i:
                corrs[:, i, j] = [np.nan_to_num(np.corrcoef(ai, aj)[0, 1])
                                  for (ai, aj) in zip(a[i].T, a[j].T)]
    return corrs

def kcca(data, reg=0., numCC=None, kernelcca=True, ktype="linear",
         gausigma=1.0, degree=2):
    """
    Set up and solve the kernel CCA eigenproblem (Canonical correlation
    analysis)
    """
    if kernelcca:
        kernel = [_make_kernel(d, ktype=ktype, gausigma=gausigma,
                               degree=degree) for d in data]
    else:
        kernel = [d.T for d in data]
    nDs = len(kernel)
    nFs = [k.shape[0] for k in kernel]
    numCC = min([k.shape[1] for k in kernel]) if numCC is None else numCC
    # Get the auto- and cross-covariance matrices
    crosscovs = [np.dot(ki, kj.T) for ki in kernel for kj in kernel]
    # Allocate left-hand side (LH) and right-hand side (RH):
    LH = np.zeros((sum(nFs), sum(nFs)))
    RH = np.zeros((sum(nFs), sum(nFs)))
    # Fill the left and right sides of the eigenvalue problem
    for i in range(nDs):
        RH[sum(nFs[:i]) : sum(nFs[:i+1]),
           sum(nFs[:i]) : sum(nFs[:i+1])] = (crosscovs[i * (nDs + 1)]
                                             + reg * np.eye(nFs[i]))
        for j in range(nDs):
            if i != j:
                LH[sum(nFs[:j]) : sum(nFs[:j+1]),
                   sum(nFs[:i]) : sum(nFs[:i+1])] = crosscovs[nDs * j + i]
    LH = (LH + LH.T) / 2.
    RH = (RH + RH.T) / 2.
    maxCC = LH.shape[0]
    r, Vs = eigh(LH, RH, eigvals=(maxCC - numCC, maxCC - 1))
    r[np.isnan(r)] = 0
    rindex = np.argsort(r)[::-1]
    comp = [] # composiiton eigenvalue solution
    Vs = Vs[:, rindex]
    for i in range(nDs):
        comp.append(Vs[sum(nFs[:i]):sum(nFs[:i + 1]), :numCC])
    nT = data[0].shape[0]
    if kernelcca:
        ws = _listdot(data, comp)
    else:
        ws = comp
    ccomp = _listdot([d.T for d in data], ws) # canonical composition
    corrs = _listcorr(ccomp)
    if corronly:
        return corrs # correlates
    else:
        return corrs, ws, ccomp # canonical variables
