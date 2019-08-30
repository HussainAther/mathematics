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
    result = np.zeros(len(x), len(u))
    for i in range(len(x)):
        for j in range(len(u)):
             result[i][j] = .5*t + x[i]*u*j
    return result

def vx(x, t):
    """
    Drift derivative.
    """
    result = np.zeros(len(x))
    for i in range(len(x)):
         result[i] = x[i]*t*.5
    return result

def vxx(x, t):
    """
    Drift derivative derivative.
    """
    result = np.zeros(len(x))
    for i in range(len(x)):
         result[i] = t*.5
    return result
    
def vt(x, u, t):
    """  
    Optimal value function. Return the minimum of a total of different
    functions. This is the first equation of the Hamilton-Jacobi-Bellman
    equations.
    """
    grandresult = []
    for i in range(t):
        grandresult.append(l(x, u, i) + np.transpose(f(x, u)) * vx(x, i) + .5*np.trace(vxx(x, t))) 
    return -min(grandresult) 
