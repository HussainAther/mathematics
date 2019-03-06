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
    n = len(a)
    theta = np.pi
    if isign == 1:
        c2 = -.5
        forwardFourier(a)
    else:
        c2 = .5
        theta = -theta
    wtemp = np.sin(.5*theta)
    wpr = -2*wtemp*wtemp
    wpi = np.sin(theta)
    wi = wpi
    for i in range(n+1):
        i1 = 2*i
        i2 = i + i1
        i3 = n - i1
        i4 = 1 + i3
        h1r = c1*(a[i1] + data[i3])
        h1i = c2*(a[i2] - data[i4])
        h2r = -c2*(data[i2] + data[i4])
        
