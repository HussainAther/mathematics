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

# for an object under the force of gravity
g = 9.81 # gravitational acceleration
l = 0.1 # initial acceleration
theta0 = 179*pi/180 # angle at which we will test

a = 0.0 # beginning position
b = 10.0 # ending position
N = 100 # number of big steps
H = (b-a)/N # size of big steps
delta = 1e-8 # required position accuracy per unit time

def f(r):
    """
    Function which we will extrapolate.
    """
    theta = r[0] # look at the first element of each array
    omega = r[1]
    ftheta = omega
    fomega = -(g/l)*sin(theta) # get our version of omega by applying our force
    return array([ftheta,fomega],float)

tpoints = arange(a,b,H)
thetapoints = []
r = array([theta0,0.0],float)

# big steps of size H
for t in tpoints:

    thetapoints.append(r[0])

    # modified midpoint step to get things started
    n = 1
    r1 = r + 0.5*H*f(r)
    r2 = r + H*f(r1)
