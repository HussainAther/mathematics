import numpy as np

"""
Use Richardson extrapolation to solve the ordinary differential equation
y'(t) = - y^2, y(0) = 1 with the trapezoidal method.
"""

ts = 0 # time start
te = 5 # time end

y0 = 1 # initial position
eps = 10e-11 # accuracy

def f(y):
    """
    Our function.
    """
    return -y**2

maxRows = 20
initialH = ts - te # step size
foundSolution = False # to check if we have a solution

h = initialH

# use the 2d matrix to hold Richardson extrapolates
a = np.zeros(maxRows, maxRows)

integratearray = []
for i in range(ts, te):
    integratearray.append(f(i))

a(1, 1) = np.trapz(integratearray, dx = h)


