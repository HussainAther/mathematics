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
    result = np.zeros(len(x), len(u))
    for i in range(len(x)):
        for j in range(len(u)):
             result[i][j] = 1 - x[i]*u*j
    return result

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

def v(x, u, t):
    """  
    Optimal value function. Return the minimum of a total of different
    functions. This is the first equation of the Hamilton-Jacobi-Bellman
    equations.
    """
    return -min(l(x, u, t) + np.transpose(f(x, u)) +  
