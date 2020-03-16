import numpy as np

from sympy import input, Symbol

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

k = np.zeros([q,q])
for i in range(1,q+1):
    for j in range(1,q+1):
        k[i-1,j-1] = np.integrate(np.diff(basis(x,i),x)*np.diff(basis(x,j),x),[x,0,1])  

f = np.zeros(q)
for i in range(1,q+1):
    f[i-1] = np.integrate(p(x)*basis(x,i),[x,0,1])+up1*basis(1,i)-up0*basis(0,i) 

c = np.linalg.solve(k,f)
solution=0
for i in range(1,q+1):
    solution = solution+c[i-1]*basis(x,i)    
x = np.linspace(0,1,100)
for i in range(1,q+1): 
    y = c[0]*basis(x,i)+c[1]*basis(x,i+1)
