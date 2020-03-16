import matplotlib.pyplot as plt
import numpy as np

from gekko import GEKKO

"""
Interpolation with Cubic Spline with GEKKO.

A cubic spline is a spline constructed of piecewise third-order polynomials 
which pass through a set of m control points. The second derivative of each 
polynomial is commonly set to zero at the endpoints, since this provides a 
boundary condition that completes the system of m-2 equations. 
"""

xm = np.array([0,1,2,3,4,5])
ym = np.array([0.1,0.2,0.3,0.5,1.0,0.9])

m = GEKKO() # Create GEKKO model
m.options.IMODE = 2 # solution mode
x = m.Param(value=np.linspace(-1,6)) # prediction points
y = m.Var() # prediction results
m.cspline(x, y, xm, ym) # cubic spline
m.solve(disp=False) # solve

# Plot.
plt.plot(xm, ym, "bo")
plt.plot(x.value, y.value, "r--", label="cubic spline")
plt.legend(loc="best")
