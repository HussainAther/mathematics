import numpy as np

from sympy import Derivative, input, integrate, Matrix, plot, solve, Symbol

"""
Rayleigh-Ritz (rayleigh ritz) method finding approximations to eigenvalue equations 
that are difficult to solve analytically, particularly in the context of solving 
physical boundary value problems that can be expressed as matrix differential equations.
"""

def basis(x,i):
    """
    Return basis function.
    """
    return x**i

x = Symbol("x")
q = input("Enter the value of q [3]: ")
y0 = input("Enter the value of y0 [0]: ")
basis = [x**i for i in range(q+1)]
ci = [Symbol("ci_%i" %i) for i in range(q+1)]
y = y0 + sum(ci[i]*basis[i] for i in range(1,q+1))
print("The trial solution is: ", u)
k = Matrix([[0,0,0],[0,0,0],[0,0,0]])
f = Matrix(1, q, range(q))
for i in range(1,q+1):
    for j in range(1,q+1):
        k[i-1,j-1] = ci[i]*ci[j]*np.diff(basis[i], x)*np.diff(basis[j], x)
for i in range(1,q+1):
    f[i-1]=2*x*ci[i]*basis[i]+ci[i]
functional= i ntegrate(sum(k.reshape(1,q**2))+sum(f),[x,0,1])
s1 = Derivative(functional,ci[1])
d1 = s1.doit()
s2 = Derivative(functional,ci[2])
d2 = s2.doit()
s3 = Derivative(functional,ci[3])
d3 = s3.doit()
xx = solve([d1,d2,d3],dict=True)
yt = y.subs(xx)
print("The Approximate Solution is: yt= ",yt)
xr = np.linspace(0,1,100)
yt = xr**3/6 - xr # The Approximate Solution
