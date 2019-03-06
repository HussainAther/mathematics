import numpy as np

"""
Calculate Fourier transform of a set of n real-valued data points.
"""

def forwardFourier(d):
    """
    Forward Fourier Transform on data d
    """
    for n in range (0 ,Np) :
        imag = 0.
        for k in range(0, N):
            imag += signal [k]∗ sin (( twopi∗k∗n) /N) # imaginary component
        d [n] = −imag∗sq2pi
        if d[n] !=0:
            impart.plot(pos=(n,d[n]))

def realFourier(a):
    """
    Perform Fourier transform on list (a) of data points.
    """
    if isign == 1:
        c2 = 0.5
        four1
