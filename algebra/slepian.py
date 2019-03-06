import numpy as np

"""
Multitaper methods use a principled approach to the trade-off between low leakage and minimizing
variance of a power spectral density estimate. Minimizing leak can let you find the tail of a spectrum
at high frequencies that can be spuriously dominated by leakage from lower frequencies.

Broadening the main lobe of the leakge function (W(s)) lets us give up some frequency resolution
(parameterized using j_res).

Multitaper models use data length N and choice j_res to solve for the best possible weights
w_j such that the ones that
"""

def slepian():
    """
    Calculate Slepian functions.
    """

