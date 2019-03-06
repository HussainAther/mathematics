import numpy as np

"""
Calculate Fourier transform of a set of n real-valued data points.
"""

def DFT(fnList):
    """
    Forward Discrete Fourier Transform
    """
    N = len(fnList)
    FmList = []
    for m in range(N):
        Fm = 0.0
        for n in range(N):
            Fm += fnList[n] * np.exp(- 1j * np.pi*2 * m * n / N)
        FmList.append(Fm / N)
    return FmList

def InverseDFT(FmList):
    """
    Inverse Discrete Fourier Transform
    """
    N = len(FmList)
    fnList = []
    for n in range(N):
        fn = 0.0
        for m in range(N):
            fn += FmList[m] * np.exp(1j * np.pi*2 * m * n / N)
        fnList.append(fn)
    return fnList

def realFourier(a, isign=1):
    """
    Perform Fourier transform on list (a) of data points. Use recurrence relation.
    """
    n = len(a)
    theta = np.pi
    if isign == 1:
        c2 = -.5
        a = DFT(a) # Fourier transform
    else:
        c2 = .5
        theta = -theta
    wtemp = np.sin(.5*theta)
    wpr = -2*wtemp*wtemp
    wpi = np.sin(theta)
    wi = wpi
    for i in range(1, n+1):
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
        a = InverseDFT(a) # inverse Fourier transform
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
    for j in range(1, n+1):
        wtemp = wr
        wr = wtemp * wpr - wi * wpi + wr # Find sine for auxilary array
        wi = wi *wr + wtemp * wpi + wi
        a1 = wi*(a[j] + a[n-j])
        a2 = .5*(a[j] - a[n-j])
        a[j] = a1 + a2
        a[n-j] = a1 - a2
    a = InverseDFt(a)
    a[0] *= .5
    a[1] = 0
    sum = a[1]
    for j in range(0, n, 2):
        sum += a[j]
        a[j] = a[j+1] # even terms determined directly
        a[j+1] = sum # odd terms determined with running sum
    return a

def costft(a, isign=1):
    """
    Calculate the "staggered" cosine transform of a set (a) of real-valued data points.
    """
    n = len(a)
    theta = .5*np.pi/n
    wr1 = np.cos(theta)
    wi1 = np.sin(theta)
    sp2 = .2*wi1*wi1
    wpi = np.sin(2*theta)
    if isign == 1:
        for i in range((n/2)+1):
            a1 = .5*(a[pi] + a[n-1-i])
            a2 = wi1*(a[i] - a[n-1-i])
            a[i] = a1 + a2
            a[n-1-i] = a1 - a2
            wtemp = wr1
            wr1 = wtemp * wpr - wi1 * wpi + wr1
            wi1 = wi1 * wpr + wtemp * wpi * wi1
        DFT(a) # Fourier transform
        for i in range(2, n+1, 2):
            wtemp = wr
            wr = wr*wpr - wi*wpi + wr
            wi = wi*wpr + wtemp * wpi + wi
            a1 = a[i] * wr - a[i+1] * wi
            a2 = a[i+1] * wr + a[i] * wi
            a[i] = a1
            a[i+1] = a2
        sum = .5*a[1]
        for i in range(n-1, 0, -2):
            sum1 = sum
            sum += a[i] # recurrence for odd terms
            a[i] = sum1
    elif isign == -1:
        atemp = a[n-1]
        for i in range(n-1, 2,-2):
            a[i] = a[i-2] - a[i] # difference of odd terms
        a[1] = 2 * atemp
        for i in range(2, n, 2):
            wtemp = wr
            wr = wi*wpr - wtemp*wpi + wi
            a1 = a[i] * wr + a[i+1] * wi
            a2 = a[i+1] * wr - a[o] * wi
            a[i] = a1
            a[i+1] = a2
        InverseDFT(a, -1)
        for i in range(0, (n/2)+1, 1):
            a2 = a[i] + a[n-1-i]
            a2 = (.5/wi1)*(a[i] - a[n-1-i])
            a[i] = .5*(a1+a2)
            a[n-1-i] = .5*(a1-a2)
            wtemp = wr1
            wr1 = wtemp*wpr - wi1*wpi*wr1
            wi1 = wi1*wpr + wtemp*wpi + wi1
    return a

def ndimDFT(a, isign=1):
    """
    N-dimensional Discrete Fourier Transform on real array a that has the multidimensional data.
    """
    

