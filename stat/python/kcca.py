def kcca(data, reg=0., numCC=None, kernelcca=True, ktype="linear",
         gausigma=1.0, degree=2):
    """
    Set up and solve the kernel CCA eigenproblem
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
    comp = []
    Vs = Vs[:, rindex]
    for i in range(nDs):
        comp.append(Vs[sum(nFs[:i]):sum(nFs[:i + 1]), :numCC])
    return comp
