import numpy as np

"""
Sequential Sparse Bayesian Learning Algorithm

In analyzing sparsity automatic relevance determination causes a subset of paramters
to be driven to zero. Sparsiy is a mechnism in the context of relevance vector machine.

If solving a regression problem, initialize beta (isotropic noise) using a basis function phi1 with hyperparameter
alpha1 set using

alphai = si^2 / (qi^2 - si)

and evaluate summation and m along with qi and si for all basis functions. Then we select a candidate
basis function phi. If qi^2 > si and alphai < infinity such that the basis vector phi is already included
in the model, update alphai using its equation. If qi^2 > si and alpha = infinity, then add phii to the model
and evaluate hyperparameter alphai = infinity. If qi^2 <= si and alphai < infinity, then remove the basis
function phi from teh model and set alphai = infinity.

Then, ff solving regression problem, update beta. If converged terminate repeat the steps of the previous paragraph.

The marginal likelihood is p(t|alpha, beta) = N(t|0, C) in which the covariance
matrix takes the form

C = (1/beta) I + (1/alpha) phi*phi^T
"""

def logistic(x):
    """
    Binary classificaiton logistic function
    """
    return 1/(1+np.exp(-x))

def mlf(x):
    """
    Multinomial link function. This lets us use multiple GLMs (multiclass) to separate
    data into more than two classes. Each class is modeled by its own set of weights,
    and the probability of a data point being a member of class c is returned.
    """
    num = np.exp(x) # numerator
    den = 0 # denominator
    for i in range(x):
        den += np.exp(x)
    return num/den

def prior(alpha, beta):
    """
    Prior distribution over the parameters being inferred. The preferred choice
    is a non-informative prior that implies that before the inferecne operation
    we hae no knowledge of what the parameters are likely to be.
    """
    return np.random.normal(beta, alpha)

def alphai(s, q):
    """
    Sparsity s and quality of phi q can be computed from the converse
    matrix and the function phi and then used to alphai.
    """
    num = s**2
    den = q**2 - s
    return num/den

def beta_binom(alpha, beta, y):
    """
    Compute the marginal likelihood, analytically, for a beta-binomial model.
    y is an array with "1" and "0" corresponding to the success and fails respectively
    """
    h = np.sum(y)
    n = len(y)
    p_y = np.exp(betaln(alpha + h, beta+n-h) - betaln(alpha, beta))
    return p_y

def ssbla(alpha, beta, phi):
    """
    Sequential Sparse Bayesian Learning Algorithm.
    """
    dist = prior(alpha, beta)


