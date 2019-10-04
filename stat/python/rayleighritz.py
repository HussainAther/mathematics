import numpy as np

from sympy import input, Matrix, Symbol

"""
Rayleigh-Ritz (rayleigh ritz) method finding approximations to eigenvalue equations 
that are difficult to solve analytically, particularly in the context of solving 
physical boundary value problems that can be expressed as matrix differential equations.
"""

x = Symbol("x")
q = input("Enter the value of q [3]: ")
y0 = input("Enter the value of y0 [0]: ")
basis = [x**i for i in range(q+1)]
ci = [Symbol("ci_%i" %i) for i in range(q+1)]
y = y0 + sum(ci[i]*np.basis[i] for i in range(1,q+1))
print("The trial solution is: ", u)
k = Matrix([[0,0,0],[0,0,0],[0,0,0]])
