import cmath
import numpy as np

from vpython.graph import color, gcurve, gidsplay, gvbars

"""
Summation of the Fourier series using two methods: sawtooth function
and half-wave function
"""

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
twopi = 2*np.pi
sq2pi = 1/np.sqrt(twopi)
h = twopi/N
dftz = np.zeros((Np), complex) # sequence complex elements

def sawtooth(signal): 
    """
    Sawtooth function
    """
    T = len(signal)
    x = 0
    for i in range(0, N+1):
        if i < T/2:
            signal[i] = (i/(T/2))
            sigfig.plot(x, signal[i]))
        else:
            signal[i] = ((i-T)/(T/2))
            sigfig.plot(x, signal[i]))

def halfwave(signal): 
    """
    Half-wave function
    """
    T = len(signal)
    x = 0
    omega = .5
    for i in range(0, N+1):
        if i < T/2:
            signal[i] = np.sin(omega*i)
            sigfig.plot(x, signal[i]))
        else:
            signal[i] = 0
            sigfig.plot(x, signal[i]))

def fourier(dftz): 
    """
    Fourier transform
    """
    for n in range(0, Np):
        zsum = complex(0, 0)
        for k in range(0, N):
            zexp = np.complex(0, twopi*k*n/N)
            zsum += signal[k] * np.exp(-zexpo)
        dftz[n] = zsum * sq2pi
        if dftz[n].imag != 0:
            impart.plot(pos=(n, dftz[n].imag))

sawtooth(signal)
fourier(dftz)

halfwave(signal)
fourier(dftz)
