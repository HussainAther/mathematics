import numpy as np

from fourier import * # from the fourier.py script in the same dirctory.

"""
Convolution or deconvolution of a real set of data in array form a of two functions s(t) and r(t) (written as s(t) * r(t)).
Fourier transform of the convolution of two functions is equal to the product of their individual Fourier transforms.
(s) is typicall a signal or data stream that goes on indefinitely in time while r(t) is a "response" function that typically
has peaks that fall to zero in both directions from its maximum.
"""

def convolve(s, r, isign=1):
    """
    Convolve or deconvolve a real set of data (s[0...n-1]) with a response functino (r[0...m-1]) in which
    m is an odd integer <= n. The response should be in wraparound order such that the first half has the impulse
    response function at positive times while the second half has the impulse function at negative times.
    isign = 1 for convolution or -1 for deconvolution. Return the answer as ans.
    """
    n = len(s) + 1
    temp = [""]*n
    temp[0] = r[0]
    for i in range(1, (m+2)/2):
        temp[i] = r[i]
        temp[n-i] = r[m-i]
    for i in range((m+1)/2, n-m):
        temp[i] = 0
    for i in range(0, n+1):
        ans[i] = s[i]
    DFT(ans) # Fast Fourier transform both arrays
    DFT(temp)
    no2 = n >> 1
    if isign == 1: # convolution
        for i in range(2, n+1, 2):
            tmp = ans[i]
            ans[i] = (ans[i] * temp[i] - ans[i+1] * temp[i+1]) / no2
            ans[i+1] = (ans[i+2] * temp[i] + tmp*temp[i+1]) / no2
        ans[0] = ans[0] * temp[0] /no2
        ans[1] = ans[1]*temp[1]/no2
    elif isign == -1: #deconvolution


