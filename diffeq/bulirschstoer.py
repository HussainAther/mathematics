import matplotlib.pyplot as plt
import numpy as np

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
theta0 = 179*np.pi/180 # angle at which we will test

a = 0.0 # beginning position
b = 10.0 # ending position
N = 100 # number of big steps
H = (b-a)/N # size of big steps
delta = 1e-8 # required position accuracy per unit time

def f(r):
    """
    Function which we will extrapolate
    """
    theta = r[0] # Look at the first element of each array.
    omega = r[1]
    ftheta = omega
    fomega = -(g/l)*np.sin(theta) # Get our version of omega by applying our force.
    return np.array([ftheta,fomega],float)

tpoints = np.arange(a,b,H)
thetapoints = []
r = np.array([theta0,0.0],float)

# big steps of size H
for t in tpoints:
    thetapoints.append(r[0])
    # modified midpoint step to get things started
    n = 1
    r1 = r + 0.5*H*f(r)
    r2 = r + H*f(r1)
    # array R1 stores the first row of the
    # extrapolation table, which contains only the single
    # modified midpoint estimate of the solution at the
    # end of the interval
    R1 = np.empty([1,2],float)
    R1[0] = 0.5*(r1 + r2 + 0.5*H*f(r2))
    # Now increase n until the required accuracy is reached.
    error = 2*H*delta
    while error>H*delta:
        n += 1
        h = H/n
        # Modified midpoint method
        r1 = r + 0.5*h*f(r)
        r2 = r + h*f(r1)
        for i in range(n-1):
            r1 += h*f(r2)
            r2 += h*f(r1)
        # Calculate extrapolation estimates. Arrays R1 and R2
        # hold the two most recent lines of the table.
        R2 = R1
        R1 = np.empty([n,2],float)
        R1[0] = 0.5*(r1 + r2 + 0.5*h*f(r2))
        for m in range(1,n):
            epsilon = (R1[m-1]-R2[m-1])/((n/(n-1))**(2*m)-1)
            R1[m] = R1[m-1] + epsilon
        error = abs(epsilon[0])
    # Set r equal to the most accurate estimate we have,
    # before moving on to the next big step.
    r = R1[n-1]

# Plot.
plt.plot(tpoints, thetapoints)
plt.show()
