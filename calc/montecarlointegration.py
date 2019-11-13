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
Integrate over a circle.
"""
