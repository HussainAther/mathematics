from numpy import *
from numpy.linalg import solve
from vpython.graph import *

"""
Provide a finite-element method solution of the one-dimensional Laplace equation via a
Galerkin spectral decomposition. Direct solution with no iteration.
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

def lin1(x, x1, x2): # hat function lol
    return (x-x1)/(x2-x1)

def lin2(x, x1, x2): # hat function in the other direction
    return (x2-x)/(x2-x1)

