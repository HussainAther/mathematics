def kcca(data, reg=0., numCC=None, kernelcca=True, ktype="linear",
         gausigma=1.0, degree=2):
    """
    Set up and solve the kernel CCA eigenproblem
    """
    if kernelcca:
        kernel = [_make_kernel(d, ktype=ktype, gausigma=gausigma,
                               degree=degree) for d in data]
    else:
