import cv2
import numpy as np
import sys
import scipy

from scipy.sparse.linalg import LinearOperator

"""
Ambrosio Tortorelli Minimizer of the Mumford-Shah functional.
Implementation of edge preserving smoothing by minimizing with 
the Ambrosio-Tortorelli appoach.
"""

def gradients(img):
    """
    Return gradients in both directions.
    """
    x = cv2.filter2D(img, cv2.CV_64F, np.array([[-1, 0, 1]]))
    y = cv2.filter2D(img, cv2.CV_64F, np.array([[-1, 0, 1]]).T)
    return x, y

def solveedges(g):
    """
    Find the edges using the linear oeprator.
    """
    size = g.shape[0]* self.g.shape[1]
    A = LinearOperator( (size, size), matvec = self.edge_linear_operator, dtype = np.float64)
    b = np.ones(size) * beta / (4 * epsilon)
    edges, _ = scipy.sparse.linalg.cg(A, b, tol = self.tol, maxiter = self.maxiter)
    return np.power(edges.reshape(*g.shape), 2)

def minimize():
    """
    Use the minimizer on the natural images.
    """
    for i in range(0, iter):
        solveedges

def justdoit(img, iter = 1, maxiter = 10, tol = 0.1, alpha = 1000, beta = 0.01, epsilon = 0.010:
    """
    Just do it. Make your dreams come true.
    """
    g = np.float64(img) / np.max(img) # smooth it over
    edges = np.zeros(img.shape)
    gradx, grady = g
    gradientmag = np.power(gradx, 2) + np.power(grady, 2) # take it to the exponent
    addconst = beta / (4 * epsilon)
    multiplyconst = epsilon * beta

img = cv2.imread(sys.argv[1], 1)
result, edges = [], []
for channel in cv2.split(img):
    # Perform the AT Minimization.
    solver = justdoit(channel, iter = 1, tol = 0.1, maxiter  = 6)
    f, v = minimize(iter)
    result.append(f)
    edges.append(v)
f = cv2.merge(result)
v = np.maximum(*edges)
show_image(v, "edges")
show_image(f, "image")
show_image(img, "original")
cv2.waitKey(-1)
