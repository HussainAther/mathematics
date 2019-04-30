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

h = initialH

# use the 2d matrix to hold Richardson extrapolates
a = np.zeros(maxRows, maxRows)

integratearray = []
for i in range(ts, te):
    integratearray.append(f(i))

# initialize with the first matrix value
a[1, 1] = np.trapz(integratearray, dx = h)

# Each row of the matrix requires one call to the trapezoid method
for i in range(1, maxRows):
    h = h/ 2
    a[i+1, 1] = np.trapz(integratearray, dx = h) # use the smaller step size h
    for j in range(1, i+1):
        a[i + 1, j + 1] = ((4^j).*a[i + 1, j] - a[i, j])/(4^j - 1) # Richardson extrapolate
    if abs(a[i+1, i+1] - a[i, i]) < eps # if the result is within our standards of accuracy
        print(y[5])
        print(a[i+1, i+1])
