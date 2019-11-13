import numpy as np
import sympy

"""
Standard Monte Carlo technique for integration is based on the mean value theorem:

I = integral from a to b of dx*f(x) = (b-a)<f>

The value of the integral of some function f(x) between a and b equals the length of the interval (b-a)
times the mean value of the function <f> over that interval. This average function can be written roughly as:

<f> ~ (1/N) * summation from i equals 1 to N of f(x_i) in which x_i is the function at i.

We can simplify these two by putting them together:

integral from a to b of dx*f(x) = (b-a)<f> = (b-a)*(1/N)*summation from i equals 1 to N of f(x_i) in which
x_i is the function at i.
"""

def x(i):
    """
    Some function x of i.
    """
    return 5*i

def f(x):
    """
    Some function f of x.
    """
    return 10*x
    
N = 10000

def mc(f, a, b): 
    """
    Monte Carlo integration of f(x) from a to b.
    """
    length = b - a
    outside = length * (1/N) # the value outside the summation
    summation = 0
    for i in range(a, b+1):
        x = x(i)
        f = f(x)
        summation += f

"""
Monte Carlo integration over domain for a double integral.
"""

def mcdouble(f, g, x0, x1, y0, y1, n):
    """
    Monte Carlo double integral for function f over domain g>=0,
    in a rectangle [x0, x1]x[y0, y1] for n^2 random points.
    """
    # Draw random points inside a rectangle.
    x = np.random.uniform(x0, x1, n)
    y = np.random.uniform(y0, y1, n)
    # Sum the f values inside the integration domain. 
    fmean = 0
    numinside = 0
    for i in range(len(x)):
        for j in range(len(y)):
            if g(x[i], y[j]) >= 0:
                numinside += 1
                fmean += f(x[i], y[j])
    fmean = fmean/float(numinside)
    area = numinside/float(n**2)*(x1-x0)*(y1-y0)
    return area*fmean

"""
Integrate over a circle.
"""

def circ(x, y):
    """
    Circle with radius 2
    """
    xc, yc = 0, 0
    R = 2
    return R**2

def mcdcircle():
    """
    Check the integral of r over a circle with radius 2.
    monte carlo circle integration.
    """
    r = sympy.symbols("r")
    Iexact = sympy.integrate(2*np.pi*r*r, (r, 0, 2))
    x0 = -2
    x1 = 2
    y0 = -2
    y1 = 2
    n = 1000
    np.random.seed(6)
    Iexpect = 16.7970837117
    Icompute = Monte
