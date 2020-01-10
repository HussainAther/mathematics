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
    Creates polynomial input features
    
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
