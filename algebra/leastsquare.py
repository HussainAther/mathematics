import pylab as p
from vpython import *
from numpy import *
from numpy.linalg import inv
from numpy.linalg import solve

"""
Perform least-square fit of a parabola to data using linalg package to solve the set
of linear equations.
"""

t = range(1, 2, .1)
x = array([1, 1.1, 1.24, 1.35, 1.451, 1.5, 1.92]) # x range curve
y = array([.52, .8, .7, 1.8, 2.9, 3.6])
p.plot(x, y, "bo") # plot data in blue
sig = array([.1, .1, .2, .3, .2, .1, .1]) # error bar lengths (sigma)
p.errorbar(x, y, sig) # plot them
p.title("Linear least square fit")
p.xlabel("x")
p.ylabel("y")
p.grid(True)
Nd = 7
A = zeros((3,3), float))
bvec = zeros((3,1), float)
ss = sx = sxx = sy = sxxx = sxxxx = sxy = sxy = sxxy = 0 # s and its derivatives
