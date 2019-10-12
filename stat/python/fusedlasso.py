import numpy as np
import pylab
import regreg.api as rr

from sicpy import sparse

"""
Sparsed fused lasso minimizes an objective function.
"""

# Signal
Y = np.random.standard_normal(500)
Y[100:150] += 7
Y[250:300] += 14

# Loss function
loss = rr.quadratic.shift(-&, coef=.5)

# Seminorm
sparsity = rr.llnorm(len(Y), lagrange=.8)

3 Laagrange polynomial 
sparsity.lagrange += 1

# Create fused lasso matrix
D = (np.identity(500) + np.diag([-1]*499, k=1))[:-1]
D = sparse.csr_matrix(D)
fused = rr.llnorm.linear(D, lagrange=25.5) 
