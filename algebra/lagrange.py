# Suppose we seek to maximize the function f(x,y)=x+y subject
# to the constraint that x2+y2=1. The function we seek to maximize
# is an unbounded plane, while the constraint is a unit circle.
# We want the maximum value of the circle, on the plane.
# We plot these two functions here.

import numpy as np

x = np.linspace(-1.5, 1.5)

[X, Y] = np.meshgrid(x, x)

import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot_surface(X, Y, X + Y)

theta = np.linspace(0,2*np.pi);
R = 1.0
x1 = R * np.cos(theta)
y1 = R * np.sin(theta)

ax.plot(x1, y1, x1 + y1, 'r-')
plt.savefig('images/lagrange-1.png')


# To find the maximum, we construct the following function:
# Λ(x,y;λ)=f(x,y)+λg(x,y) where g(x,y)=x2+y2−1=0, which is the constraint function.
# Since g(x,y)=0, we are not really changing the original function, provided that
# the constraint is met!

import numpy as np

def func(X):
    x = X[0]
    y = X[1]
    L = X[2] # this is the multiplier. lambda is a reserved keyword in python
    return x + y + L * (x**2 + y**2 - 1)

# The minima/maxima of the augmented function are located where all of
# the partial derivatives of the augmented function are equal to zero,
# i.e. ∂Λ/∂x=0, ∂Λ/∂y=0, and ∂Λ/∂λ=0. the process for solving this is
# usually to analytically evaluate the partial derivatives, and then
# solve the unconstrained resulting equations, which may be nonlinear.

# Rather than perform the analytical differentiation,
# here we develop a way to numerically approximate the partial derivatives.

def dfunc(X):
    dLambda = np.zeros(len(X))
    h = 1e-3 # this is the step size used in the finite difference.
    for i in range(len(X)):
        dX = np.zeros(len(X))
        dX[i] = h
        dLambda[i] = (func(X+dX)-func(X-dX))/(2*h);
    return dLambda

# The function we defined above (dfunc) will equal zero
# at a maximum or minimum. It turns out there are two solutions to
# this problem, but only one of them is the maximum value.
# Which solution you get depends on the initial guess provided to the solver.
# Here we have to use some judgement to identify the maximum.

from scipy.optimize import fsolve

# this is the max
X1 = fsolve(dfunc, [1, 1, 0])
print X1, func(X1)

# this is the min
X2 = fsolve(dfunc, [-1, -1, 0])
print X2, func(X2)

# Three dimensional plots in matplotlib are a little more difficult
# than in Matlab (where the code is almost the same as 2D plots,
# just different commands, e.g. plot vs plot3). In Matplotlib
# you have to import additional modules in the right order, and
# use the object oriented approach to plotting as shown here.


# Lagrange interpolation takes equations and fits them to data to try
# to understand how well they fit. Lagrange himself figured out that
# a closed-form formula can directly fit the (n-1)-order polynomial given by:
# g(x) ~ a0 + a1 * x + a2 * x**2 + ... + a_n-1 * x**n-1
# We can re-write this as:
# g(z) ~ g1*λ1 + g2λ2 + ... + gnλn
# in which lambda is the product of each (x-xj) / (xi - xj) from j = 1 to j = n.
# The difference between teh polynomial evaluated at some x and that of the actual function is
# R_n ~ ((x-x1)(x-x2)...(x-xn))/(n!) * (g**n) * ζ in which ζ  is undetermined.
# This shows that significantly high derivates can't be approximated well by a polynomial.

#def lagrange_interpolation(g, x, m): # WORK IN PROGRESS!!!
#    """
#    Perform Lagrange interpolation using g(x) ~ a0 + a1 * x + a2 * x**2 + ... + a_n-1 * x**n-1
#    in which g is the function, x is the point to evaluate, and m is the maximum number of terms to use.
#    """
#    totalsum = 0
#    xj = x + 1
#    xi = x + .1
#    l = (x-xj) / (xi - xj) # l is lambda
#    for i in range(1, max+1):
#        for j in range(1, n+1):
#            xj = x + 1*j
#            xi = x + .1*j
#            l *= (x-xj) / (xi - xj)
#        totalsum += * g(x) * l
#    return totalsum

def lagrange (x ,i , xm ):
    """
    Evaluates the i-th Lagrange polynomial at x
    based on grid data xm
    """
    n=len( xm )-1
    y=1
    for j in range ( n+1 ):
        if i!=j:
            y*=( x-xm[j])/( xm[i]-xm[j])
    return y

def interpolation (x , xm , ym ):
    """
    Fit our lagrange function to actual data
    """
    n=len( xm )-1
    lagrpoly = array ([ lagrange (x ,i , xm ) for i in range ( n+1 )])
    y = dot( ym , lagrpoly )
    return y
