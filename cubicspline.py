import numpy as np
import matplotlib.pyplot as plt
from gekko import GEKKO

"""
Interpolation with Cubic Spline
"""

xm = np.array([0,1,2,3,4,5])
ym = np.array([0.1,0.2,0.3,0.5,1.0,0.9])

m = GEKKO()             # create GEKKO model
m.options.IMODE = 2     # solution mode
x = m.Param(value=np.linspace(-1,6)) # prediction points
y = m.Var()             # prediction results
m.cspline(x, y, xm, ym) # cubic spline
m.solve(disp=False)     # solve

# create plot
plt.plot(xm,ym,'bo')
plt.plot(x.value,y.value,'r--',label='cubic spline')
plt.legend(loc='best')
