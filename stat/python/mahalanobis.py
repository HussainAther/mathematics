import numpy as np

"""
Mahalanobis distance.
"""

xx = []
yy = []

X = np.vstack([xx,yy])
V = np.cov(X.T)
VI = np.linalg.inv(V)
m = np.diag(np.sqrt(np.dot(np.dot((xx-yy),VI),(xx-yy).T)))
