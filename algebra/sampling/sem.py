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
        X = np.asarray(X) # make sure we're using a numpy array
        self.m, self.n = X.shape # get the size
        self.data = X.copy() # to refer to again later
        # number of mixtures
        self.k = k # can be adjusted. haven't messed around so much

    def _init(self):
        """
        Initialize the various values pertaining to the data set.
        """
        # init mixture means/sigmas
        self.mean_arr = np.asmatrix(np.random.random((self.k, self.n))) # mean (average) from the Gaussian distribution
        self.sigma_arr = np.array([np.asmatrix(np.identity(self.n)) for i in range(self.k)]) # variance (sigma)
        self.phi = np.ones(self.k)/self.k # phi function used in expectation maximization
        self.w = np.asmatrix(np.empty((self.m, self.k), dtype=float)) # 

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

    def e_step(self):
        """
        Expectation step for each weight such that we get the tight lower bound.
        Maximize the expectation value.
        """
        # calculate w_j^{(i)}
        for i in range(self.m):
            den = 0
            for j in range(self.k):
                num = sp.stats.multivariate_normal.pdf(self.data[i, :],
                                                       self.mean_arr[j].A1,
                                                       self.sigma_arr[j]) *\
                      self.phi[j]
                den += num
                self.w[i, j] = num
            self.w[i, :] /= den
            assert self.w[i, :].sum() - 1 < 1e-4

    def m_step(self):
        """
        Update the paramters such that we maximize the lower bound.
        Don't forget to check out sigma and mean for the solution.
        """
        for j in range(self.k):
            const = self.w[:, j].sum()
            self.phi[j] = 1/self.m * const
            _mu_j = np.zeros(self.n)
            _sigma_j = np.zeros((self.n, self.n))
            for i in range(self.m):
                _mu_j += (self.data[i, :] * self.w[i, j])
                _sigma_j += self.w[i, j] * ((self.data[i, :] - self.mean_arr[j, :]).T * (self.data[i, :] - self.mean_arr[j, :]))
            self.mean_arr[j] = _mu_j / const
            self.sigma_arr[j] = _sigma_j / const

