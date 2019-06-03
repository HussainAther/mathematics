import numpy as np

from fourier import DFT

"""
Similar to convolution, correlation represents two functions by different but generally similar data sets
and investigates their "correlation" by comparing them both directly superposed and with one of them
shifted either right or left.

The discrete correlation theorem says that this discrete correlation of two real functions g and h
is one membeer of the discrete Fourier transform pair

Corr(g, h)+j <=> G_k H_k*

in which G_k and H_k are discrete Fourier transforms of g_j and h_j. The * denotes complex conjugation.
"""

def corr(a, b):
    """
    Compute correlation of two real data sets a and b of same length. The length n must bea n integer power of 2.
    The answer is returned in ans.
    """
    n = len(a)
    temp = [""]*n
    ans = [""]*n
    if len(a) != len(b):
        print("a and b must be same length.")
        return
    for i in range(0, n+1):
        ans[i] = a[i]
        temp[i] = b[i]
    DFT(ans) # transform both vectors
    DFT(temp)
    no2 = n >> 1 # normalizatino for inverse FFT
    for i in range(2, n+1, 2):
        tmp = ans[i]
        ans[i] = (ans[i] * temp[i] + ans[i+1] * temp[i+1])/n02
        ans[i+1] = (ans[i+1]*temp[i] - tmp*temp[i+1])/ no2
    ans[0] = ans[0] * temp[0]/no2
    ans[1] = ans[1] * temp[1]/no2
    InverseDFT(ans) # get the correlation from inverse transformation
    return ans

