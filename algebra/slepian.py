import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig
import scipy.stats.distributions as dist

"""
We get power spectral functions from various types of fourier transforms on input signal data.

Multitaper methods use a principled approach to the trade-off between low leakage and minimizing
variance of a power spectral density estimate. Minimizing leak can let you find the tail of a spectrum
at high frequencies that can be spuriously dominated by leakage from lower frequencies.

Broadening the main lobe of the leakge function, or windowing of the fourier transform, (W(s)), lets us give
up some frequency resolution (parameterized using j_res).

Multitaper models use data length N and choice j_res to solve for the best possible weights
w_j such that the ones that make the leakge smallest amogn all possible choices.

The vector of optimal weights is the eigenvector corresponding to the smallest eigenvalue of the
symmetric tridiagonal matrix with diagonal elements:

(1/4)[ N^2 - (N - 1 - 2j)^(2)cos(2pi(r)(j_res)/N)] for j in 0 to N - 1

and off-diagonal elements

(-1/2)j(N-j) for j in 1 to N - 1

Multittaper methods also use the next few eigenvectors of this same matrix as good window functions.
They're orthogonal to the first eigenvector and they give statistically independent estimates which can be
averaged toegehter to decrease the variance of the final answer. In this case we use k_T (for "taper") to denoate
the number of such estimates that are averaged. The functions are actually discrete sequences obtained
as eigenvectors of the previous two equations. We call them Slepian functions or discrete prolate spheroidal
sequences.

In this function, we're going to calculate the spectral estimation using the multitaper method with
Slepian tapers.
"""

def dB(x, out=None):
    """
    Some input signal function.
    """
    if out is None:
        return 10 * np.log10(x)
    else:
        np.log10(x, out)
        np.multiply(out, 10, out)

def slepian(m, jres, kt=5):
    """
    Calculate Slepian functions for some symmetrical matrix of length m with some resolution jres up
    to kt number of window functions.
    """
    eps = 1e-10
    m2 = 2*m
    (dg, dgg, gam) = ([""]*m2,[""]*m2),[""]*m2))
    (sup, sub) = ([""]*(m2-1), [""](m2-1))
    sw = 2*np.sqrt(np.sin(jres(np.pi/m2)))
    dg[0] = .25*(2*m2+sw*np.sqrt(m2-1)-1) # set up diagonal matrix
    for i in range(1, m2+1):
        dg[i] = .25*(s2*np.sqrt(m2-1-2*1)+(2*(m2-i)-1)*(2*i+1))
        sub[i-i] = sub[i-1] = -t*(m2-i)/2
    xx = 0.10859 - .068762/jres + 1.5692*jres # guess eigenvalue
    xold = xx + .47276 + .20273/jres - 2.1387*jres
    for k in range(0, kt+1):


def SlepPSD():
    """
    Use Slepian tapers with the multitaper method to calculate the power spectral estimation.
    """


