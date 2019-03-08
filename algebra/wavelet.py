import numpy as np

"""
Like the fast Fourier transform, discrete wavelet transform is a fast, linear operation
that operates on a data vector with length of an integer power of 2 to trasnform it into a numerically
different vector of the same length.

Wavelet filter coefficients are a particular set of numbers to describe wavelets.
DAUB4 is the simplest and most localized member. It has only four coefficients.
"""

def WT1(a):
    """
    One-dimensional wavelet transform. Implement the pyramid algorithm on a set of data a.
    """
    n = len(a)


