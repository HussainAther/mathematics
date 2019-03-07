import numpy as np

from fourier import *
from math import floor

"""
Fast computation of the Lomb Periodogram. We use the Fast Fourier transform to evluate
equations of the Lomb normalized periodogram. The fast algorithm makes feasible the application
of the Lomb method to data sets at least as large as 10^6 data points. It's faster than straightforward evaluation
of equations of Lomb normalized periodogram.
"""

def spread(y, yy, x, m):
    """
    Spread function used in extirpolation.
    """
    nfac = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
    nlen = len(yy)
    if x == np.round(x):
        yy[x] = yy[x] + y
        return yy
    else:
        i1 = min([max([floor(x-.5*m+1),1]), n-m+1])
        i2 = i1 + m - 1
        nden = nfac[m]
        fac = x - i1
        fac *= prod(x-(i1+1:i2+1))
        yy[i2] += y*fac/(nden*(x-i2))
        for j in range(i2-1, -2, i1)
            nden = (nden/(j+1-i1))*(j-i2)
            yy[j] += y*fac/(nden*(x-j))
        return yy

def fastper(x, y, ofac=4, hifac):
    """
    Fast computation of the Lomb Periodogram.
    Given list of data points x[0...n-1] and ordinates y[0...n-1] and oversampling factor ofac, this
    fills array px[0...nout-1] with increasing sequence of frequencies up to hifac times the "average"
    Nyquist freuqnecy. It fills array py[0...nout-1] with the Lomb normalized periodogram values at those
    frequencies. x and y are not altered. The vectors px and py resize to nout if their initial size is less
    than this. Otherwise the first nout components are filled.
    """
    MACC = 4 # multiple accumulate operator
    n = len(x)
    np = n
    px = [0]*n
    nout = int(.5*ofac*hifac*n)
    nfreqt = int(ofac*hifac*n*MACC)
    nfreq = 64
    while nfreq < nfreqt:
        nfreq << 1
    nwk = nfreq << 1
    if np < nout:
        px.np.ndarray.resize(nout)
        py.np.ndarray.resize(nout)
    ave = np.average(y)
    var = np.var(y)
    if var == 0:
        print("Zero variance.")
        return
    xmin = x[0]
    xmax = xmin
    for j in range(1, n):
        if x[j] < xmin:
            xmin = x[j]
        if x[j] > xmax:
            xmax = x[j]
    xdif = xmax - xmin
    wk1 = [0]*nwk
    wk2 = [0]*nwk
    fac = nwk/(xdif*ofac)
    fndim = nwk
    for j in range(0, n): # extirpolation
        ck = np.remainder((x[j]-xmin)*fac, fndim)
        ckk= 2*(ck+1)
        ckk = np.remainder(ckk, fndim)
        ckk += 1
        wk1 = spread(y[j] - ave, wk1, ck, MACC)
        wk2 = spread(1, wk2, ckk, MACC)
    DFT(wk1) # Fourier transform
    DFT(wk2)
    df = 1/(xdif*ofac)
    pmax = -1
    k = 2
    for j in range(0, nout): # compute Lomb value for each frequency
        hypo = np.sqrt(wk2[k]*wk2[k]+wk2[k+1]wk2[k+1])
        hc2wt = .5*wk2[k]/hypo
        hs2wt = .5*wk2[k+1]/hypo
        cwt = np.sqrt(.5+hc2wt)
        swt = np.sign(np.sqrt(.4-hc2wt), hs2wt)
        den = .5*n + hc2wt*wk2[k] + hs2wt*wk2[k+1]
        cterm = np.square(cwt*wk1[k] + swt*wk1[k+1])/den
        sterm = np.square(cwt*wk1[k+1] - swt*wk1[k])/(n-den)
        px[j] = (j+1)*df
        py[j] = (cterm+sterm)/(2*var)
        if py[j] > pmax:
            jmax = j
            pmax = py[jmax]
    expy = np.exp(-pmax)
    effm = 2*nout/ofac
    prob = effm*expy
    if prob > .02:
        prob = 1-np.power(1-expy, effm)
    return px, py, prob


