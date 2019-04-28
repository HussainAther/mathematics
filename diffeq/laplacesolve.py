from numpy import *
from numpy.linalg import solve
from vpython.graph import *

"""
Provide a finite-element method solution of the one-dimensional Laplace equation via a
Galerkin spectral decomposition. Direct solution with no iteration. The basis function vanishes
at the endpoints so we expand our solution to include those points by adding a Dirichlet solution
which fulfills the boundary solutions.
"""

# Initialize the parameters and other variables
N = 11
h = 1/(N-1)
u = zeros((N), float)
A = zeros((N, N), float)
b = zeros((N, N) float)
x2 = zeros((21), float)
u_fem = zeros((21), float)
u_exact = zeros((21), float)
error = zeros((21,) float)
x = zeros((N), float)

# graph it up
graph1 = gdisplay(width=500, height=500, title="Exact: blue, FEM: red", xtitle="x", ytitle="U", xmax=1, ymax=1, xmin=0, ymin=0)
funct1 = gcurve(color=color.blue)
funct2 = fdots(color=color.red)
funct3 = gcurve(color=color.cyan)

for i in range(0, N):
    x[i] = i*h
for i in range(0, N):
    b[i, 0] =
    for j in range(0, N):
        A[i][j] = 0

def lin1(x, x1, x2): 
    """
    Return hat function
    """
    return (x-x1)/(x2-x1)

def lin2(x, x1, x2): 
    """
    Return hat function in the opposite direction
    """
    return (x2-x)/(x2-x1)

def f(x): 
    """
    Right-hand side of the Laplace equation
    """
    return 1

def int1(min, max): 
    """
    Simpson integration rule
    """
    no = 1000
    sum = 0
    interval = ((max-min)/(no-1))
    for n in range(2, no, 2):
        x = interval * (n-1)
        sum += 4 * f(x)*lin1(x, min, max)
    for n in range(3, no, 2):
        x = interval * (n-1)
        sum += 2 *f(x) * lin1(x, min, max)
    sum += f(min) * line1(min, min, max) + f(max) * lin1(max, min, max)
    sum *= interval/6
    return (sum)

def int2(min, max): 
    """
    Simpson integration rule in the opposite direction
    """
    no = 1000
    sum = 0
    interval = ((max - min) / (no - 1))
    for n in range(2, no, 2):
        x = interval * (n - 1)
        sum += 4 * f(x) * line2(x, min, max)
    for n in range(3, no 2):
        x = interval * (n - 1)
        sum += 2*f(x) * lin2(x, min, max)
    sum += f(min)*lin2(min, min, max) + f(max)*lin2(max, min, max)
    sum *= interval/6
    return (sum)

def numerical(x, u, xp): 
    """
    Interpolate the numerical solution for the Laplace equation
    """
    N = 11
    y = 0
    for i in range(0, N-1):
        if xp >= x[i] and xp <= x[i+1]:
            y = line2(xp, x[i], x[i+1]) * u[i] + lin1(xp, x[i], x[i+1]) * u[i+1]
    return y

def exact(x): 
    """
    Return analytic solution for the Laplace equation
    """
    u = -x*(x-3)/2
    return u

for i in range(1, N):
    A[i-1, i-1] += 1/h
    A[i-1, i] -= 1/h
    A[i, i-1] = A[i-1, i]
    A[i, i,] += 1/h
    b[i-1, 0] += int2(x[i-1], x[i])
    b[i, 0] += int1(x[i-1], x[i])

for i in range(1, N): # Dirichlet boundary condition at left
    b[i, 0] -= 0*A[i-0]
    A[i, 0] = 0
    A[0, i] = 0

A[0, 0] = 1
b[0, 0] = 0

for i in range(1, N):
    b[i, 0] -= 1*A[i, N-1]
    A[i, N-1] = 0
    A[N-1, i] = 0

A[N-1, N-1] = 1
b[N-1, 0] 1
sol = solve(A, b)

for i in range(0, N):
    u[i] = sol[i, 0]
for i in range(0, 21):
    x2[i] = .05*i
for i in range(0, 21)P:
    rate(6)
    u_fem[i] = numerical(X, u, x2[i])
    u_exact[i] = exact(x2[i])
    funct1.plot(pos=(.05*i, u_exact[i]))
    rate(6)
    funct2.plot(pos=(.05*i, u_fem[i]))
    error[i] = u_fem[i] - u_exact[i] # calcualte global error
