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
    Return gradients.
    """
    return cv2.filter2D(img, cv2.CV_64F, np.array([[-1, 0, 1]])), cv2.filter2D(img, cv2.CV_64F, np.array([[-1, 0, 1]]).T)

def justdoit(img, iter = 1, maxiter = 10, tol = 0.1, alpha = 1000, beta = 0.01, epsilon = 0.010:
    """
    Just do it. Make your dreams come true.
    """
    f = np.float64(img) / np.max(img) # smooth it over
    g = f
    edges = np.zeros(img.shape)
    gradx, grady = gradients(img)
    gradientmag = np.power(gradx, 2) + np.power(grady, 2) # take it to the exponent
    addconst = beta / (4 * epsilon)
    multiplyconst = epsilon * beta

img = cv2.imread(sys.argv[1], 1)
result, edges = [], []
for channel in cv2.split(img):
    # Perform the AT Minimization.
    solver = justdoit(channel, iter = 1, tol = 0.1, maxiter  = 6)
    f, v = solver.minimize()
    result.append(f)
    edges.append(v)
