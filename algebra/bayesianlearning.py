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

def alphai(i, t1, t2):
    """
    Sparsity s and quality of phi q can be computed from the converse
    matrix and the function phi and then used to alphai. This is used
    to update alpha as needed
    """
    num = si(phi, alpha, beta,i)**2
    den = qi(phi, alpha, beta, t1, t2, i)**2 - si(phi, alpha, beta,i)
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

def C(phi, alpha, beta, i):
    """
    Covariance matrix of the marginal likelihood.
    """
    phiT = np.transpose(phi[i])
    I = np.identity(len(alpha))
    beta_in = np.linalg.inv(beta)
    imax = range(len(alpha))
    summed = 0
    for j in range(len(alpha)):
        if j != i:
            summed += np.linalg.inv(alpha[j])*phi[j]*np.tranpose(phi[j]) + np.linalg.inv(alpha[i])*phi[i]*phiT[i]
    return beta_in*I + summed

def qi(phi, alpha, beta, t1, t2, i):
    """
    Quality of phi_i.
    """
    return np.transpose(phi[i])*np.linalg.inv(C(phi[-i], alpha, beta, i))*np.transpose(t1, t2)

def si(phi, alpha, beta, i):
    """
    Sparsity of phi_i.
    """
    return np.tranpose(phi[i])*C(phi[-i], alpha, beta, i)*phi[i]

def ssbla(model, alpha, beta, phi, t1, t2, regression=True):
    """
    Sequential Sparse Bayesian Learning Algorithm, as described above.
    model is a list of our model functions.
    """
    dist = prior(alpha, beta)
    for i in range(len(alpha)):
        if qi(phi, alpha, beta, i, t1, t2)**2 > s(phi, alpha, beta,i) and alpha[i] < np.inf:
            alpha[i] = alphai(i, t1, t2) # update alpha[i] using the alphai function
        elif qi(phi, alpha, beta, i, t1, t2)**2 > (phi, alpha, beta,i) and alpha[i] == np.inf:
            model.append([phi[i], alphai(i, t1, t2)]) # add phi_i to the model and evaluate alphai hyperparameter
        elif qi(phi, alpha, beta, i, t1, t2)**2 <= s(phi, alpha, beta,i) and alpha[i] < np.inf:
            model.pop(phi[i])
    if regression:
        dist = prior(alpha, beta)
    return models, dist

"""
Sequential Monte Carlo progresses with successive interpolated
sequences from the prior to the posterior. We get an estimation of the
marginal likelihood.
"""
n_chains = 1000

models = []
traces = []
for alpha, beta in priors:
    with pm.Model() as model:
        a = pm.Beta('a', alpha, beta)
        yl = pm.Bernoulli('yl', a, observed=y)
        trace = pm.sample(1000,
                          step=pm.SMC(),
                          random_seed=42)
        models.append(model)
        traces.append(trace)
