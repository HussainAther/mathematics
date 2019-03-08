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
def WTFilter(a, nn):
    result = []
    count = 0
    for i in range(

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
            wlet.filt(a, nn, isign) # start from largest hierarchy and work toward smallest
    else:
        for nn in range(n, 4):
            wlet.filt(a, nn, isign) # from smallest and work upward
        wlet.condition(a,n, -1)
    return wlet


