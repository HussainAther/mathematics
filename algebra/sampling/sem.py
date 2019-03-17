import numpy as np
import scipy as sp

import seaborn as sns
from matplotlib import pyplot as plt
"""
With the supplemental expectation maximization algorithm, we get the covariance matrix by
using only the code for computing the complete-data covariance matrix, the code for the expectation
maximization itself, and the code for standard matrix operations.
"""
class GMM(object): # Gaussian mixture model
    def __init__(self, X, k=2):
        """
        Initialize the Gaussian mixture model with a set of data X.
        """
        # dimension
        X = np.asarray(X)
        self.m, self.n = X.shape
        self.data = X.copy()
        # number of mixtures
        self.k = k

    def _init(self):
        """
        Initialize the various values pertaining to the data set.
        """
        # init mixture means/sigmas
        self.mean_arr = np.asmatrix(np.random.random((self.k, self.n)))
        self.sigma_arr = np.array([np.asmatrix(np.identity(self.n)) for i in range(self.k)])
        self.phi = np.ones(self.k)/self.k
        self.w = np.asmatrix(np.empty((self.m, self.k), dtype=float))
        #print(self.mean_arr)
        #print(self.sigma_arr)

    def fit(self, tol=1e-4):
        """
        Fit the model using the log likelihood function.
        """
        self._init()
        num_iters = 0
        ll = 1
        previous_ll = 0
        while(ll-previous_ll > tol):
            previous_ll = self.loglikelihood()
            self._fit()
            num_iters += 1
            ll = self.loglikelihood()
            print("Iteration %d: log-likelihood is %.6f"%(num_iters, ll))
        print("Terminate at %d-th iteration:log-likelihood is %.6f"%(num_iters, ll))

    def loglikelihood(self):
        """
        Borrow the log likelihood from statistics in determining the best way to fit.
        """
        ll = 0
        for i in range(self.m):
            tmp = 0
            for j in range(self.k):
                #print(self.sigma_arr[j])
                tmp += sp.stats.multivariate_normal.pdf(self.data[i, :],
                                                        self.mean_arr[j, :].A1,
                                                        self.sigma_arr[j, :]) *\
                       self.phi[j]
            ll += np.log(tmp)
        return ll


    def _fit(self):
        """
        Execute both the E (expectation) and M (maximization) steps.
        """
        self.e_step()
        self.m_step()

    
