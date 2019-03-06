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

def slepian():
    """
    Use Slepian tapers with the multitaper method to calculate the power spectral estimation.
    """
    

