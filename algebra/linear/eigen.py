import numpy as np

from numpy.linalg import eig

"""
Solve the matrix eigenvalue problem.
"""

# change this to whatever matrix to solve.
I = array( [[2/3, -1/4, -1/4], [-1/4, 2/3, -1/4], [-1/4, -1/4, 2/3]])

# set eigenvalues and evectors from the matrix.
Es, evectors = eig(I)

# get vectors
Vec = array([evectors[0, 0,], evectors[1, 0], evectors[2, 0]])

# Set the left-hand side and right-hand side of the equations equal to one another
LHS = np.dot(I, Vec)
RHS = np.dot(Vec, Es[0])
print(LHS - RHS)

"""
Power iteration is a straightforward approach for two matrices A and B.
"""

A = np.matrix([[4, -5],[2,-2]])
B = np.matrix([[2,1,0,0],[1,2,0,0],[1,1,1,0],[0,-2,2,-1]])

# Choose a random vector
rando = np.random.rand(A.shape[1]) 

# Number of iterations or simulations
n = 100 
for i in range(n):
    # Calculate the norm of the matrix-by-vector product
    norm = np.linalg.norm(np.dot(A, rando))
    # Apply to the vector 
    rando =/ norm
print("Power iteration result " + str(rando)) 
