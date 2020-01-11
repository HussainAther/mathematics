import numpy as np
import matplotlib.pyplot as plt
import torch

from scipy.special import gamma as gf
from torch import tensor
from torch.distributions.normal import Normal
from torch.distributions.gamma import Gamma
from torch.distributions.multivariate_normal import MultivariateNormal as MN
from torch.distributions.uniform import Uniform

"""
Bayesian inference in generative models

In this tutorial, we write several different inference methods for a simple Bayesian linear regression model. 

1. Defining the generative model
2. Exact posterior inference
3. Markov Chain Monte Carlo using Metropolis Hastings
4. Classic variational inference using a mean-field approximation
5. Stochastic variational inference
    
"""

"""
1. Defining the generative model 

> Prior p(lambda)p(beta | lambda)
tau ~ Gamma(a_0, b_0) # Precision
beta_k ~ Normal(m_0, 1/tau**0.5) # Coefficient for x^k
> Likelihood p(y | beta, x, tau)
y ~ Normal(beta.T x, 1/tau*I)

more details: https://en.wikipedia.org/wiki/Bayesian_linear_regression
"""

print("~~~Defining priors~~~")
def tau_prior(a_0, b_0):
    """
    Prior over the precision, i.e., tau = 1/sigma^2 
    
    To sample variance:
    variance = 1./tau_prior(a_0, b_0).sample()
    """
    return Gamma(a_0, b_0)

def betas_prior(mu_0, variance):
    """
    Prior over polynomial weights
    
    To sample k beta weights:
    betas = betas_prior(mu_0, variance).sample(sample_shape=torch.Size([k]))
    
    If comparing to wikipedia, here we"ve set lambda_0 = 1.0
    """
    return Normal(mu_0, 1e-7 + variance**0.5)

print("~~~Defining likelihood~~~")
def loglikelihood(y, b, x, variance):
    """
    p(y | b, x, sigma^2) = N(y | mu = f(b,x), sigma^2)
    
    Inputs
    ------
    y: (n,) tensor 
    b: (k,) tensor of weights
    x: (n,k) input features
    variance: scalar 
    
    Output
    ------
    Log probability of y"s
        
    """
    return MN(x.mm(b[:,None]),(1e-7 + variance)*torch.eye(len(y))).log_prob(y)

def features(_x, k):
    """
    Create polynomial input features.
    
    Input
    -----
    _x: (n,) vector of x-coordinates
    k: order of polynomial
    
    Output
    ------
    x: (n, k) tensor
    """
    x = torch.ones(len(_x), 1)
    for i in range(1,k):
        feature = _x**i 
        x = torch.cat((x, feature[:, None]), 1)
    return x

def sample_from_prior(x, a_0, b_0, mu_0, k):
    """
    Returns sample of y"s given x-coordinates and prior params.
    """
    x = features(x, k)
    variance = 1./tau_prior(a_0, b_0).sample()
    betas = betas_prior(mu_0, variance).sample(sample_shape=torch.Size([k]))
    y = Normal(x.mm(betas[:, None]), variance**0.5).sample()
    return y, betas

## Sample from the prior 
print("~~~Sampling from the prior~~~")
x_list = [-2 + i*0.1 for i in range(41)]; x = tensor(x_list); x_arr = np.array(x_list)
a_0 = tensor(0.5); b_0 = tensor(0.5); mu_0=tensor(0.); k=4;
y, betas = sample_from_prior(x, a_0, b_0, mu_0, k)
polynomial_str = ""
for i, b in enumerate(betas.numpy()):
    polynomial_str += "{0:.2f}".format(b) + "x^" + str(i) 
    if i < k - 1: polynomial_str += " + "
plt.scatter(x_arr, y.numpy()); plt.title(polynomial_str); plt.show()

"""
2. Exact posterior inference

Since we are using conjugate priors, it is possible to compute the posterior analytically.
The form of the posterior will be the same as the prior: 
- Gaussian distribution over betas
- Gamma distribution over precision

You can find the derivation on the wikipedia page.

"""
print("~~~Defining the posterior~~~")
def analytical_posterior(y, x, a_0, b_0, mu_0, k):
    """
    Given a dataset (x,y), return posterior parameters 
    for p(b | sigma^2, y, x) and p(precision | y, x).
    
    Inputs
    ------
    y: (n,) tensor 
    x: (n,) x-coordinates
    a_0, b_0, mu_0: prior parameters
    k: order of polynomial 
    
    Outputs
    -------
    a_posterior: () shape parameter for Gamma dist
    b_posterior: () scale parameter for Gamma dist
    mu_posterior: (k,) mean
    lambda_posterior: (k,k) precision matrix
    
    """
    
    x = features(x, k)
    
    ##p(b|tau, y, x) = N(mu_posterior, (1/tau)*lambda_posterior^-1)
    XTX = x.t().mm(x)
    lambda_0 = torch.eye(k)
    lambda_posterior = XTX + lambda_0
    lambda_inv = lambda_posterior.inverse()
    
    mu_0 = mu_0*torch.ones(k,1)
    inside = lambda_0.mm(mu_0) + x.t().mm(y)
    mu_posterior = lambda_inv.mm(inside)
        
    ##p(tau| y, X)
    a_posterior = a_0 + len(y)/2.
    mlm = mu_0.t().mm(lambda_0).mm(mu_0) - mu_posterior.t().mm(lambda_posterior).mm(mu_posterior)
    b_posterior = b_0 + 0.5*(y.t().mm(y) + mlm)
    
    return a_posterior, b_posterior, mu_posterior, lambda_posterior
