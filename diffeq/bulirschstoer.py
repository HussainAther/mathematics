from math import sin, pi
from numpy import empty, array, arange
from pylab import plot, show

"""
In numerical analysis, the Bulirsch–Stoer algorithm is a method for the numerical solution of
ordinary differential equations which combines three powerful ideas: Richardson extrapolation,
the use of rational function extrapolation in Richardson-type applications, and the modified
midpoint method, to obtain numerical solutions to ordinary differential equations (ODEs)
with high accuracy and comparatively little computational effort. It is named after Roland
Bulirsch and Josef Stoer. It is sometimes called the Gragg–Bulirsch–Stoer (GBS) algorithm
because of the importance of a result about the error function of the modified midpoint method,
due to William B. Gragg.
"""

g = 9.81 # gravitational acceleration
l = 0.1 # length
theta0 = 179*pi/180 #

a = 0.0 # beginning position
b = 10.0 # ending position
N = 100 # number of big steps
H = (b-a)/N # size of big steps
delta = 1e-8 # required position accuracy per unit time

def f(r):
    """
    """
    theta = r[0]
    omega = r[1]
    ftheta = omega
    fomega = -(g/l)*sin(theta)
    return array([ftheta,fomega],float)
