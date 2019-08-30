import numpy as np

"""
Hamilton-Jacobi-Bellman (HJB) hamilton jacobi bellman equations for controlled
ito diffusion. Use an n-dimensional Browniawn motion as a stochastic differential
equation.
"""

def f(x, u):
    """
    Drift.
    """
    return x*u

def F(x, u):
    """
    Diffusion coefficient.
    """
    return 2

dt = .5
dw = .5    
# Sample differential formula for drift and diffusion 
dx = f(x, u) * dt + F(x, y) * dw 

def l(x, u, t):
    """
    Cost rate.
    """
    return x*u*t*.5

def v(x, yu, t):
    """  
    Optimal value function. Return the minimum of a total of different
    functions. This is the first equation of the Hamilton-Jacobi-Bellman
    equations.
    """
    return -min(l(x, u, t) + f(x, u) 
