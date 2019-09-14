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
