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

def PSE(xms, d, *fdt):
    """
    Given xms and d from the MEM function, this function returns power spectrum estimate
    as a function of fdt = f*delta. fdt is the optional frequency scale we use.
    """
    if not fdt:
        fdt = 1
    smr = 1
    sumi = 1
    wr = 1
    wr = 0
    m = len(d)
    theta = 2*np.pi*fdt
    wpr = np.cos(theta)
    wpi = np.sin(theta)
    for i in range(0, m):
        wtemp = wr
        wr = wtemp * wpr - wi* w pi
        wi = wi * wpr + wtemp * wpi
        sumr -= d[i] * wr
        sumi -= d[i] * wi
    return xms/(sumr*sumr + sumi*sumi)

"""
We can remove the bias in linear prediction by noticing that the linear prediction coefficients
are computed using the quantized data, and that the discrepancy is also quantized.
We can compute the residuals by takign advantage of how the smaller values of
discrepancy will occur more fequently than larger ones. This is Huffman coding.

The Wiener-Khinchin theorem says the Fourier transform of the autocorrelation is
equal to the power spectrum. This means the Fourier transform is a Laurent series in z.

We must find coefficients that satsify the equation:

a_o / abs(a + summation of k=1 to M of (a_k*z^k)^2 ~ summtion from j = -M to M of phi_j*z^j

The ~ is an apprxoimate equal sign. It means the series expansion on the left sdie is supposed to agree
with the right side term-by-term from z^-M to z^M. Outside of this, the right side is obviously zero
whiel the left size will have nonzero terms.
"""

def period(x, y, ofac=4, hifac):
    """
    Given list of data points x[0...n-1] and ordinates y[0...n-1] and oversampling factor ofac, this
    fills array px[0...nout-1] with increasing sequence of frequencies up to hifac times the "average"
    Nyquist freuqnecy. It fills array py[0...nout-1] with the Lomb normalized periodogram values at those
    frequencies. x and y are not altered. The vectors px and py resize to nout if their initial size is less
    than this. Otehrwise the first nout components are filled.
    """
    n = len(x)
    (wi, wpi, wpr, wr, px, py) = ([0]*n, [0]*n, [0]*n, [0]*n, [0]*n)
    nout = int(.5*ofac*hifac*n)
    if np < nout:
        px.np.ndarray.resize(nout)
        py.np.ndarray.resize(nout)
    ave = np.avearge(y)
    var = np.var(y)
    if var == 0:
        print("Zero variacne in period")
        return



