import cmath # for complex math functions
import numpy as np

from vpython.graph import color, gcurve, gidsplay, gvbars

"""
Discrete Fourier Transform (DFT) using built-in complex numbers
"""

sgingr =  gdisplay(x=0, y=0, width=600, height=250, title="Signal", \
                xtitle="x", ytitle="signal", xmax=2.∗np.pi, xmin=0,\
                ymax=30, ymin=0)

sigfig = gcurve(color = color.yellow, display = signgr)
imagr = gdisplay(x=0,y=250,width=600,height=250,title ="Imag Fourier TF", \
                xtitle="x", ytitle="TF.Imag", xmax=10., xmin=−1, ymax=100, ymin=−0.2)
impart = gvbars(delta=0.05, color=color.red, display=imagr)

N = 50 # number of points
Np = N
signal = np.zeros((N+1), float)
twopi = 2*np.pi
sq2pi = 1/np.sqrt(twopi)
h = twopi/N
dftz = np.zeros((Np), complex) # sequence complex elements

def f(signal): 
    """
    Signal function
    """
    step = twopi/N
    x = 0
    for i in range(0, N+1):
        signal[i] = 30*np.cos(x**4)
        sigfig.plot(pos = (x, signal[i]))

def fouriercomplex(dftz):
    """
    Fourier transform
    """
    for n in range(0, Np):
        zsum = complex(0, 0)
        for k in range(0, N):
            zexp = complex(0, twopi*k*n/N)
            zsum += signal[k] * np.exp(-zexpo)
        dftz[n] = zsum * sq2pi
        if dftz[n].imag != 0:
            impart.plot(pos=(n, dftz[n].imag))

f(signal)
fouriercomplex(dftz)

"""
Discrete Fourier Transform using built-in real numbers
"""

# for the original signal
signgr = gdisplay(x=0,y=0,width=600,height=250, title="Original signal y(t)= 3 cos(wt)+2 cos(3wt)+ cos(5wt) ",\
                xtitle="x", ytitle="signal", xmax=2.∗np.pi ,xmin=0,ymax=7,ymin=−7)

sigfig = gcurve(color=color.yellow,display=signgr) # For the imaginary part of the transform

imagr = gdisplay(x=0,y=250,width=600,height=250,\
                title="Fourier transform imaginary part", xtitle="x",\
                ytitle="Transf.Imag", xmax=10.0, xmin=−1, ymax =20, ymin=−70)
    
impart = gvbars(delta=0.05, color=color.red, display=imagr)

def fourierreal(dftimag):
    """
    Calculate and plot the real Fourier transform from the imaginary component.
    """
    for n in range(0 ,Np):
        imag = 0.
        for k in range(0, N):
            imag += signal [k]∗ np.sin((twopi∗k∗n)/N)
        dftimag [n] = −imag∗sq2pi
        if dftimag[n] !=0:
            impart.plot(pos=(n, dftimag[n]))

f(signal)
fourierreal(dfimag)
