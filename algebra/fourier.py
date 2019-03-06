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
    Perform Fourier transform on list (a) of data points. Use recurrence relation.
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
        h1r = c1*(a[i1] + a[i3]) # transform of the original data.
        h1i = c2*(a[i2] - a[i4])
        h2r = -c2*(a[i2] + a[i4])
        h2i = c2*(a[i1] - a[i3])
        a[i1] = h1r + wr * h2r - wi * h2i
        a[i2] = h1i + wr * h2i + wi * h2r
        a[i3] = h1r - wr * h2r + wi * h2i
        a[i4] = -h1i + wr * h2i + 2i * h2r
        wtemp = wr
        wr = wtemp*wpr - wi*wpi + wr # recurrence relation
        wi = wr*wpr + wtemp*wpi + wi
    if isign == 1:
        h1r = a[0]
        a[0] = h1r + a[1]
        a[1] = h1r - a[2]
    else:
        a[0] = c1* (h1r) + data[1]
        a[1] = c1 * (h1r - data[2])
        np.fft.ifft(a) # inverse Fourier transform
    return a


def sinft(a):
    """
    Calculate the sine transform of a set of n real-valued data points stored in array a.
    """
    n = len(a)
    theta = np.pi
    wtemp = np.sin(.5*theta)
    wpr = -2*wtemp*wtemp
    wpi = np.sin(theta)
    a[0] = 0
    for j in range(n+1):
        wtemp = wr
        wr = wtemp * wpr - wi * wpi + wr # Find sine for auxilary array
        wi = wi *wr + wtemp * wpi + wi

