import numpy as np

"""
Functions to calculate integration points and weights for Gaussian quadrature.

x,w = gaussxwab(N,a,b) returns integration points and weights
    mapped to the interval [a,b], so that sum_i w[i]*f(x[i])
    is the Nth-order Gaussian approximation to the integral
    int_a^b f(x) dx

This code finds the zeros of the nth Legendre polynomial using
Newton's method, starting from the approximation given in Abramowitz
and Stegun. The Legendre polynomial itself is evaluated
using the recurrence relation given in Abramowitz and Stegun.
"""

def gaussxw(N):
    """
    x,w = gaussxw(N) returns integration points x and integration
    weights w such that sum_i w[i]*f(x[i]) is the Nth-order
    Gaussian approximation to the integral int_{-1}^1 f(x) dx
    """

    # Initial approximation to roots of the Legendre polynomial
    a = linspace(3,4*N-1,N)/(4*N+2)
    x = cos(pi*a+1/(8*N*N*tan(a)))

    # Find roots using Newton's method
    epsilon = 1e-15
    delta = 1.0
    while delta>epsilon:
        p0 = ones(N,float)
        p1 = copy(x)
        for k in range(1,N):
            p0,p1 = p1,((2*k+1)*x*p1-k*p0)/(k+1)
        dp = (N+1)*(p0-x*p1)/(1-x*x)
        dx = p1/dp
        x -= dx
        delta = max(abs(dx))
