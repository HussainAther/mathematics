import numpy as np

from sympy import input, Symbol, 

"""
Galerkin Method to solve the second-order boundary value problem
d^2u/dx^2 + p(x) = 0, u(0) = 0, du/dx(1) = up1=1
"""

def p(x):
    """
    Function of interest.
    """
    return x   

def basis(x,i):
    """
    Basis function.
    """
    return x**i

x = Symbol("x")
q = input("Enter the value of q: ")
u0, up0, up1 = input("Enter the boundary conditions [u0,up0,up1]: ")


