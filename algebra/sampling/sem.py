import numpy as np
import random
"""
With the supplemental expectation maximization algorithm, we get the covariance matrix by
using only the code for computing the complete-data covariance matrix, the code for the expectation
maximization itself, and the code for standard matrix operations.
"""
class GMM(object):
    def __init__(self, X, k=2):
        # dimension
        X = np.asarray(X)
        self.m, self.n = X.shape
        self.data = X.copy()
        # number of mixtures
        self.k = k

