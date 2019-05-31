import pylab as pl
import numpy as np
import vpython as vp

"""
Perform least-square fit of a parabola to data using linalg package to solve the set
of linear equations.
"""

# initialize data
t = arange(1, 2, .1) # time range
x = array([1, 1.1, 1.24, 1.35, 1.451, 1.5, 1.92]) # x range curve
y = array([.52, .8, .7, 1.8, 2.9, 3.6])
pl.plot(x, y, "bo") # plot data in blue
sig = array([.1, .1, .2, .3, .2, .1, .1]) # error bar lengths (sigma)
pl.errorbar(x, y, sig) # plot them
pl.title("Linear least square fit")
pl.xlabel("x")
pl.ylabel("y")
pl.grid(True)
Nd = 7
A = np.zeros((3,3), float))
bvec = np.zeros((3,1), float)
ss = sx = sxx = sy = sxxx = sxxxx = sxy = sxy = sxxy = 0 # s and its derivatives

for i in range(0, Nd):
    sig2 = sig[i] * sig[i]
    ss += 1/sig2
    sx += x[i]/sig2
    sy += y[i]/sig2
    rh1 = x[i]*x[i]
    sxx += rh1/sig2
    sxxy += rh1 * y[i]/sig2
    sxy += x[i]*y[i]/sig2
    sxxx += rh1*x[i]/sig2
    sxxxx += rh1*rh1/sig2

A = array([[ss, sx, sxx], [sx, sxx, sxxx], [sxx, sxxx, sxxx]])
bvec = array([sy, sxy, sxxy])

xvec = np.multiply(np.linalg.inv(A), bvec)
Itest = np.multiply(A, np.linalg.inv(A))
print("\n x vector via inverse" + str(xvec) + "\n")
print("A*inverse(A) " + Itest + "\n")

xvec = np.linalg.solve(A, bvec) # Solve via elimination
print("x Matrix via direct" + str(xvec))

for i in range(0, Nd):
    s = xvec[0] + xvec[1]*x[i] + xvec[2]*x[i]*x[i]
    print(" %d %5.3f %5.3f %8.7f \n" %(i, x[i], y[i], x))
    
curve = xvec[0] + xvec[1]*t + xvec[2]*t**2
points = xvec[0] + xvec[1]*c + xvec[2]*x**2
pl.plot(t, curve, "r", x, points, "ro") # Plot the fit line in red
pl.show()
