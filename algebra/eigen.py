from numpy import *
from numpy.linalg import eig

"""
Solve the matrix eigenvalue problem
"""

# change this to whatever matrix to solve.
I = array( [[2/3, -1/4, -1/4], [-1/4, 2/3, -1/4], [-1/4, -1/4, 2/3]])

# set eigenvalues and evectors from the matrix.
Es, evectors = eig(I)

# get vectors
Vec = array([evectors[0, 0,], evectors[1, 0], evectors[2, 0]])

# Set the left-hand side and right-hand side of the equations equal to one another
LHS = dot(I, Vec)
RHS = dot(Vec, Es[0])
print(LHS - RHS)
