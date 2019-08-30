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
    
# Sample differential formula for drift and diffusion 
dx = f(x, u) * dt + F(x, y) * dw 

def v(l, f, vx, tr):
    """  
    Optimal value function. Return the minimum of a total of different
    functions. This is the first equation of the Hamilton-Jacobi-Bellman
    equations.
    """

