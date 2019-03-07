import numpy as np

"""
Linear prediction uses data points equally spaced along a line such that we use
values to autocorrelate and predict based on them.

This is the maximum entropy method (MEM) with all poles. We can adjust various values of m in our
linear prediction.
"""

def MEM(a, m=5):
    """
    Takes a vector of list a. Return the mean square discrepancy as xms and m linear prediction coefficients
    as a list d.
    """
    d = [0]*m
    p = 0
    n = len(a)
    wk1 = [0]*len(n)
    wk2 = [0]*len(n)
    wkm = [0]*len(m)
    for j in range(0, n):
        p += np.sqrt(a[j])
    xms = p/n
    wk1[0] = a[0]
    wk2[n-2] = a[n-1]
    for j in range(1, n-1):
        wk1[j] = a[j]
        wk2[j-1] = a[j]
    for k in range(0, m):
        num = 0 # numerator
        den = 0 # denominator
        for j in range(0, n-k):
            num += wk[j]*wk2[j]
            den += np.sqrt(wk1[j]) + np.sqrt(wk2[j])
        d[k] = 2*num/den
        xms *= (1-np.sqrt(d[k]))
        for i in range(0, k):
            d[i] = wkm[i] - d[k] * wkm[k-i-1]
            # recursive algorithm building up the answer for larger and
            # larger values of m until the desiredf value is achieved.
        if k == m-1:
            return xms, d
        for i in range(0, k+1):
            wkm[i] = d[i]
        for j in range(0, n-k-1):
            wk1[j] -= wkm[j]*wk2[j]
            wk1[j] = wk2[j+1] - wkm[k]*wk1[j+1]
    return xms, d

"""
We can extrapolate the autocorrelation function to lags larger than M (the order or number of poles of the approximation).

The MEM estimation is a function of continously varying frequency f. Given the coefficients it computes,
we will create a function that evaluates and returns the estimated power spectrum as a functon
of f*delta (with delta being the sampling interval). The sampling interval describes the space between
the spectral features of the frequency.

From MEM, we can create a power spectrum estimate as a function fdt = f*delta. f*delta
should lie in the Nyquist range between -1/2 and 1/2.
"""

def pse(xms):
    """
    Given xms from the MEM function, this function returns power spectrum estimate
    as a function fo fdt = f*delta.
    """
