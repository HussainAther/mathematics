import numpy as np

"""
Like the fast Fourier transform (FFT), discrete wavelet transform (DWT) is a fast, linear operation
that operates on a data vector with length of an integer power of 2 to trasnform it into a numerically
different vector of the same length.

Wavelet filter coefficients are a particular set of numbers to describe wavelets.
DAUB4 is the simplest and most localized member. It has only four coefficients. DAubs and Daub4i are
other examples.

DWT applies the pyramidal algorithm: wavelet coefficient matrix hierarchically, first to the full data vector of length n, then to
the "smooth" vector of length n/2, then to the "smooth-smooth" vector of length n/4, and so on until a trivial
number of smooth components remain. It outputs the remaining components and all the "detail" components
that were accumulated along the way.
"""
def haarMatrix(n, normalized=False):
    """
    Haar matrix also used in some forms of DFT analysis.
    """
    # Allow only size n of power 2
    n = 2**np.ceil(np.log2(n))
    if n > 2:
        h = haarMatrix(n / 2)
    else:
        return np.array([[1, 1], [1, -1]])

    # calculate upper haar part
    h_n = np.kron(h, [1, 1])
    # calculate lower haar part
    if normalized:
        h_i = np.sqrt(n/2)*np.kron(np.eye(len(h)), [1, -1])
    else:
        h_i = np.kron(np.eye(len(h)), [1, -1])
    # combine parts
    h = np.vstack((h_n, h_i))
    return h

def wletFilter(a, nn):
    return

def WT1(a, isign):
    """
    One-dimensional wavelet transform. Implement the pyramid algorithm on a set of data a.
    """
    n = len(a)
    if n <4:
        print("a must be larger than three members")
        return
    if isign > 0: # wavelet transform
        wlet.condition(a,n,1)
        for nn in range(n, 5):
            wletFilter(a, nn, isign) # start from largest hierarchy and work toward smallest
    else:
        for nn in range(n, 4):
            wletFilter(a, nn, isign) # from smallest and work upward
    return wlet


