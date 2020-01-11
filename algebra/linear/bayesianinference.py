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

# Sample from the prior 
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
    
    # p(b|tau, y, x) = N(mu_posterior, (1/tau)*lambda_posterior^-1)
    XTX = x.t().mm(x)
    lambda_0 = torch.eye(k)
    lambda_posterior = XTX + lambda_0
    lambda_inv = lambda_posterior.inverse()
    
    mu_0 = mu_0*torch.ones(k,1)
    inside = lambda_0.mm(mu_0) + x.t().mm(y)
    mu_posterior = lambda_inv.mm(inside)
        
    #p(tau| y, X)
    a_posterior = a_0 + len(y)/2.
    mlm = mu_0.t().mm(lambda_0).mm(mu_0) - mu_posterior.t().mm(lambda_posterior).mm(mu_posterior)
    b_posterior = b_0 + 0.5*(y.t().mm(y) + mlm)
    
    return a_posterior, b_posterior, mu_posterior, lambda_posterior

def polynomial(bs, x):
    """
    Return a polynomial of degree x with coefficients bs.
    """
    m = np.zeros(len(x))
    for i, b in enumerate(bs):
        m += b*(x**i)
    return m

def sample_from_posterior(x, a, b, mu, lmbda):
    """
    Sample betas from the posterior distribution.
    """
    variance = 1./Gamma(a, b).sample()
    betas = MN(mu.squeeze(), variance*lmbda.inverse()).sample()
    return polynomial(betas.numpy(), x)
    
# Inference given sampled y
inferred_a, inferred_b, inferred_mu, inferred_lambda = analytical_posterior(y, x, a_0, a_0, mu_0, k)
print("Inferred a: ", inferred_a.numpy())
print("Inferred b: ", inferred_b.squeeze().numpy())
analytical_inferred_mu = inferred_mu.squeeze().numpy();
print("Inferred mu: ", analytical_inferred_mu); 
print("Inferred precision (note dependence between betas): ")
print(inferred_lambda.numpy()) 

print("How do samples from the posterior look compared to the data?")
plt.scatter(x_arr, y.numpy()); plt.title("Actual: " + polynomial_str); 
for i in range(100):
    plt.plot(x_arr,sample_from_posterior(x, inferred_a, 
                            inferred_b, inferred_mu, inferred_lambda), alpha=0.02, color="blue")
plt.xlim(min(x_list),max(x_list))
plt.show()

print("We can also check predictions outside of the range of our dataset:")
x_list_extr = [-3 + i*0.1 for i in range(61)]; x_extr = tensor(x_list_extr);
plt.scatter(x_arr, y.numpy());
for i in range(100):
    plt.plot(x_list_extr,sample_from_posterior(x_extr, inferred_a, 
                            inferred_b, inferred_mu, inferred_lambda), alpha=0.02, color="blue")
plt.xlim(min(x_list_extr),max(x_list_extr))
plt.show()

"""
3. Markov Chain Monte Carlo using Metropolis Hastings

First we'll define a function to make proposals and 
calculate necessary probabilities, given approximate distributions
Then we'll fill out the specifics of our MH algorithm 
"""

def propose(transition_dist, prior, prev_val):
    """
    General purpose proposal function
    
    Inputs
    ------
    prev_val: the previous sample, z
    transition_dist: a function that takes in a val and returns a distribution --> q(z | val)
    prior: the prior over val --> p(z)
    
    Outputs
    -------
    new_val: new proposed value, z'
    prior_logprob: log probability of new_val under its prior p
    ft_logprob: transition probability from prev_val to new_val --> log q(z'|z)
    bt_logprob: transition probability from new_val to prev_val --> log q(z|z')
    
    """
    new_val = transition_dist.sample()
    prior_logprob = prior.log_prob(new_val)
    ft_logprob = transition_dist.log_prob(new_val)
    bt_logprob = transition_dist.log_prob(prev_val)
    return new_val, prior_logprob, ft_logprob, bt_logprob      

"""
To write our MH algorithm, we need to:

1. Initialize the chain at z_0
2. Define transition distributions q(z'|z)
3. Sample from q(z'|z)
4. Compute the acceptance probability
5. Decide whether to accept the proposal as a sample

"""