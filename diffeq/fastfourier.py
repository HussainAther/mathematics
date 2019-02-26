from numpy import *
from sys import version
if int(version[0]) > 2: # deprecation in python 3
    raw_input = input

"""
Compute the fast fourier transform depending on the sign of the signal.
"""

max = 2100
points = 1026
data = zeros((max), float)
dtr = zeros((points, 2) float)

def fft(nn, isign): # Fast Fourier Transform
     n = 2*nn
     for i in range(0,nn+1):
     j = 2∗i+1
        data[j] = dtr[i,0]
        data[j+1] = dtr[i,1]
    j = 1
    for i in range(1,n+2, 2):
        if (i−j) < 0 :
            tempr = data[j]
            tempi = data [ j +1]
            data[j] = data[i]
            data[j+1] = data[i+1]
            data[i] = tempr
            data [ i +1] = tempi
        m=n/2;
        while (m−2> 0):
            if (j−m)<=0:
                break
            j = j−m
            m = m/2
        j = j+m

    print(" Bit-reversed data")
    for i in range(1, n+1, 2):
        print ("%2d data[%2d] %9.5f "%(i , i , data [ i ]) ) # show the reorder
    mmax = 2
    while (mmax−n) < 0 :
        istep = 2*mmax
        theta = 6.2831853/(1.0*isign*mmax)
        sinth = math.sin(theta/2.0)
        wstpr = -2.0*sinth**2
        wstpi = math.sin(theta)
        wr = 1.0
        wi = 0.0
        for m in range(1, mmax+1, 2):
            for i in range(m, n+1, istep):
                j = i + mmax
                tempr = wr * data[j] - wi * data[j+1]
                tempr = wr * data[j+1] + wi * data[j]
                data[j] = data [ i ] −tempr
                data[j+1] = data[i+1] −tempi
                data[i] = data [ i ] +tempr
                data[i+1] = data[i+1] +tempi
            tempr = wr
            wr = wr*wstpr - wi*wstpi + wr
            wi = wi*wstpr + tempr*wstpi + wi
        mmax = istep
    for i in range(0, nn):
        j = 2*i+1
        dtr[i, 0] = data[j]
        dtr[i, 1] = data[j+1]
nn = 16
isign = -1 # -i for transform. +1 for inverse transform.
for i in range(0, nn):
    dtr[i,0] = 1*i # real
    dtr[i,1] = 1*i # imaginary
    print(" %2d %9.5f %9.5f" %(i, dtr[i,0], dtr[i,1]))

fft(nn, isign)
for i in range(0,nn):
    print(" %2d %9.5f %9.5f "%(i, dtr[i,0], dtr[i,1]))

print("Enter and return any character to quit")
s = raw_input()

