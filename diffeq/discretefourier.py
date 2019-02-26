from vpython.graph import *
import cmath # for complex math functions
import numpy as np

# discretefourier.py: Discrete Fourier Transform using built-in complex numbers

sgingr =  gdisplay(x=0, y=0, width=600, height=250, title ="Signal", \
                xtitle="x", ytitle = "signal", xmax = 2.∗math.pi, xmin = 0,\
                ymax = 30, ymin = 0)

sigfig = gcurve(color = color.yellow, display = signgr)
imagr = gdisplay(x=0,y=250,width=600,height=250,title ="Imag Fourier TF", \
                xtitle = "x", ytitle="TF.Imag",xmax=10.,xmin=−1,ymax=100,ymin=−0.2)
impart = gvbars(delta = 0.05, color = color.red, display = imagr)

N = 50 # number of points
Np = N
signal = np.zeros((N+1), float)
twopi = 2*pi
sq2pi = 1/sqrt(twopi)
h = twopi/N
dftz = np.zeros((Np), complex) # sequence complex elements

def f(signal): # signal function
    step = twopi/N
    x = 0
    for i in range(0, N+1):
        signal[i] = 30*cos(x**4)
        sigfig.plot(pos = (x, signal[i]))

def fourier(dftz): # fourier transform
    for n in range(0, Np):
        zsum = complex(0, 0)
        for k in range(0, N):
            zexp = complex(0, twopi*k*n/N)
            zsum += signal[k] * exp(-zexpo)
        dftz[n] = zsum * sq2pi
        if dftz[n].imag != 0:
            impart.plot(pos=(n, dftz[n].imag))

f(signal)
fourier(dftz)
