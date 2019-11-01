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
    f, v = solver.minimize()
    result.append(f)
    edges.append(v)
f = cv2.merge(result)
v = np.maximum(*edges)
show_image(v, "edges")
show_image(f, "image")
show_image(img, "original")
cv2.waitKey(-1)
