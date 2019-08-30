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
    
# Sample differential formula for drift and 
dx = f(x, u) * dt + F(x, y) * dw 
