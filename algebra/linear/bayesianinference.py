import numpy as np
import matplotlib.pyplot as plt
import torch

from scipy.special import gamma as gf
from torch import tensor
from torch.distributions.normal import Normal
from torch.distributions.gamma import Gamma
from torch.distributions.multivariate_normal import MultivariateNormal as MN
from torch.distributions.uniform import Uniform
from torch.optim import Adam
from torch.nn import Parameter

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
    Log probability of y's
        
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
x_list = [-2 + i*0.1 for i in range(41)]
 x = tensor(x_list)
 x_arr = np.array(x_list)
a_0 = tensor(0.5) 
b_0 = tensor(0.5) 
mu_0=tensor(0.) 
k=4
y, betas = sample_from_prior(x, a_0, b_0, mu_0, k)
polynomial_str = ""
for i, b in enumerate(betas.np()):
    polynomial_str += "{0:.2f}".format(b) + "x^" + str(i) 
    if i < k - 1: polynomial_str += " + "
plt.scatter(x_arr, y.np())
 plt.title(polynomial_str)
  plt.show()

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
    return polynomial(betas.np(), x)
    
# Inference given sampled y
inferred_a, inferred_b, inferred_mu, inferred_lambda = analytical_posterior(y, x, a_0, a_0, mu_0, k)
print("Inferred a: ", inferred_a.np())
print("Inferred b: ", inferred_b.squeeze().np())
analytical_inferred_mu = inferred_mu.squeeze().np()
print("Inferred mu: ", analytical_inferred_mu)
print("Inferred precision (note dependence between betas): ")
print(inferred_lambda.np()) 

print("How do samples from the posterior look compared to the data?")
plt.scatter(x_arr, y.np())
plt.title("Actual: " + polynomial_str)
for i in range(100):
    plt.plot(x_arr,sample_from_posterior(x, inferred_a, 
                            inferred_b, inferred_mu, inferred_lambda), alpha=0.02, color="blue")
plt.xlim(min(x_list),max(x_list))
plt.show()

print("We can also check predictions outside of the range of our dataset:")
x_list_extr = [-3 + i*0.1 for i in range(61)]
 x_extr = tensor(x_list_extr)
plt.scatter(x_arr, y.np())
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
    # Get proposal value and log q(z'|z)
    forward_dist = transition_dist(prev_val)
    new_val = forward_dist.sample()
    ft_logprob = forward_dist.log_prob(new_val)
    # log q(z|z')
    backward_dist = transition_dist(new_val)
    bt_logprob = backward_dist.log_prob(prev_val)
    # log p(z)
    prior_logprob = prior.log_prob(new_val)
    return new_val, prior_logprob, ft_logprob, bt_logprob       

"""
To write our MH algorithm, we need to:

1. Initialize the chain at z_0
2. Define transition distributions q(z'|z)
3. Sample from q(z'|z)
4. Compute the acceptance probability
5. Decide whether to accept the proposal as a sample

"""

def MH(y, x, k, a_0, b_0, mu_0, n_iterations):
    
    x_features = features(x,k)
    
    # Define the priors, p(tau) * p(beta | tau).
    t_prior = tau_prior(a_0, b_0)
    b_prior = lambda variance: betas_prior(mu_0, variance)

    # Storage for samples
    tau_samples = []
    betas_samples = []

    # Initialize latent variables at prior mean.
    tau = t_prior.mean
    betas = torch.ones(k) * b_prior(1./tau).mean
    
    for i in range(n_iterations):
        
        # Calculate the unnormalized posterior (joint pdf) for the previous latents, p(z, x).
        tau_logprob = t_prior.log_prob(tau)
        betas_logprob = b_prior(1./tau).log_prob(betas)
        ll = loglikelihood(y, betas, x_features, 1./tau)
        log_p_z_given_x = torch.sum(tau_logprob) + torch.sum(betas_logprob) + torch.sum(ll)
                
        # Propose new latent variables.
        # We will implement a "single-site" Metropolis Hastings algorithm.
        # From iteration to iteration, alternate between proposing a new tau or new betas.
        if i % 2 == 0:
        
            def transition_dist(old_tau):
                min_val = min(pv.numpy(),0)
                max_val = pv + 1.
                return Uniform(min_val, max_val)
            tau_prime, tau_logprob, ft_logprob, bt_logprob = propose(transition_dist, t_prior, tau)
            betas_prime = betas 
            betas_logprob = b_prior(1./tau_prime).log_prob(betas_prime) 
        else:
            tau_prime = tau
            def transition_dist(old_betas):
                return MN(pv.squeeze(), torch.eye(k)*1e-2)
            betas_prime, betas_logprob, ft_logprob, bt_logprob = propose(transition_dist, b_prior(1./tau_prime), betas)

        # Compute the log likelihood of the new sampled latents.
        ll = loglikelihood(y, betas_prime, x_features, 1./tau_prime)
        # Combine the log probabilities to get the unnormalized posterior for the current latents, p(z' | x).
        log_p_zprime_given_x = torch.sum(tau_logprob) + torch.sum(betas_logprob) + torch.sum(ll)
        
        # Compute the acceptance/
        # log acceptance = log(p(z' | x)) + q(z' | z) - log(p(z | x)) - p(z | z')
        log_acceptance = log_p_zprime_given_x + ft_logprob - log_p_z_given_x - bt_logprob
        acceptance = torch.exp(log_acceptance)
        
        # Decide whether to accept the new latents by the MH algorithm.
        r = min(acceptance.numpy(),1)
        u = Uniform(0,1).sample()
        if u.numpy() < r:
            tau = tau_prime
            betas = betas_prime
        tau_samples.append(tau.numpy())
        betas_samples.append(betas.numpy())        
            
    return tau_samples, betas_samples

n_iterations = 3000
tau_samples, betas_samples = MH(y, x, k, a_0, b_0, mu_0, n_iterations)
plt.scatter(x_list, y.numpy())
plt.title("Actual: " + polynomial_str)
burn_in = 100; lag = 10

# Plot sampled posterior mean betas.
total_samples = 0; 
for i in range(burn_in,n_iterations,lag):
    b = betas_samples[i] if total_samples == 0 else b + betas_samples[i]
    total_samples += 1
    plt.plot(x_list_extr,polynomial(betas_samples[i], np.array(x_list_extr)), alpha=0.01, color="blue")
plt.xlim(min(x_list_extr),max(x_list_extr))
print("MCMC (expectation): ")
MCMC_expectation = (b*1./total_samples).tolist()
print(MCMC_expectation)
print("Analytical: ")
print(analytical_inferred_mu)
plt.show()  

"""
Variational inference

1. Derive the evidence lower bound
2. Derive updates from the bound
3. Write iterative updates to variational parameters 

"""

def elbo_lambda(a, b, a_0, b_0):
    p1 = (a - a_0)*torch.digamma(a) 
    p2 = -torch.lgamma(a) + torch.lgamma(a_0)
    p3 = a_0*(torch.log(b) - torch.log(b_0))
    p4 = a*(b_0 - b)/b
    return -(p1 + p2 + p3 + p4)
    
def elbo_beta(a, b, nu, omega, mu_0):
    p1 = 0.5*(a/b)*(nu - mu_0)**2
    p2 = 0.5*(a/(b*omega) - 1. - torch.digamma(a) + torch.log(b) + torch.log(omega))
    return -torch.sum(p1 + p2)

def elbo_y(a, b, nu, omega, x, y):
    p1 = len(y) * 0.5*(torch.digamma(a) - torch.log(b) - torch.log(tensor(2*np.pi)))
    p2 = torch.sum(-(a/(2.*b))*(y**2), dim=0)
    p3 = torch.sum((a/b)*y.squeeze()*torch.sum(x * nu[None, :], dim=1),dim=0)
    p4 = torch.sum(torch.sum( x**2*(1./omega + nu**2)[None, :], dim=1),dim=0)
    x_expand = x[:, :, None]
    x_expand_T = x[:, None,:]
    nu_expand = nu[None, :, None]
    nu_expand_T = nu[None, None, :]
    t = torch.sum(x_expand*x_expand_T*nu_expand*nu_expand_T,dim=0)
    p5 = 2*(t.triu().sum() - t.trace())
    p6 = -(a/(2.*b))*(p4 + p5)
    return p1 + p2 + p3 + p6

def compute_elbo(a, b, nu, omega, x, y, a_0, b_0, mu_0):
    L = elbo_lambda(a, b, a_0, b_0); 
    B = elbo_beta(a, b, nu, omega, mu_0);
    Y = elbo_y(a, b, nu, omega, x, y);
    return  L + B + Y

    def update_omega(a, b, x):
    return (a/b)*(1 + torch.sum(x**2, dim=0))

def update_nu_k(a, b, nu, x, y, k):
    K = x.size(1)
    denom = 1. + torch.sum(x[:, k]**2, dim = 0)
    p0 = mu_0
    p1 = torch.sum( y.squeeze() * x[:, k] )
    p3 = -torch.sum(
        sum(x[:,k] * x[:,j] * nu[j] for j in range(K) if j != k)
    )
    return (p0 + p1 + p3) / denom

def update_b(nu, omega, x, y):
    
    p1 = tensor(gf(1.5) * 2**(1.5) / np.sqrt(2*np.pi))/omega
    p2 = (nu - mu_0)**2
    p3 = 0.5*torch.sum(p1 + p2)
    
    p4 = 0.5*torch.sum(y.squeeze()**2)
    
    p5 = torch.sum(x * nu[None, :], dim=1)
    p6 = -torch.sum(y.squeeze()*p5)
    
    p7 = torch.sum(x**2*(1./omega + nu**2)[None,:])
    t = torch.sum(x[:, :, None]*x[:, None,:]*nu[None, :, None]*nu[None, None, :],dim=0)
    p8 = 2*(t.triu().sum() - t.trace())
    p9 = 0.5*(p7 + p8)
    
    return b_0 + p3 + p4 + p6 + p9

def variational_inference(x, y, a_0, b_0, mu_0, k, n_iterations=10):
    
    x = features(x,k)
    
    # We'll check that the elbo increases with each update.
    elbos = []
    
    # Initialize latent variables.
    a = (k + 1. + len(y))/2. + a_0 #a does not get updated further
    b = b_0
    omega = Uniform(0.5, 1.5).sample(sample_shape=torch.Size([k]))
    nu = Normal(0,1).sample(sample_shape=torch.Size([k]))
    
    # Start iterative updates.
    for i in range(n_iterations):
        # Update b.
        b = update_b(nu, omega, x, y)
        elbos.append(compute_elbo(a, b, nu, omega, x, y, a_0, b_0, mu_0).numpy()[0])
        # Update omega.
        omega = update_omega(a, b, x)
        elbos.append(compute_elbo(a, b, nu, omega, x, y, a_0, b_0, mu_0).numpy()[0])
        # Update each nu in turn.
        for _k in range(k):
            nu[_k] = update_nu_k(a, b, nu, x, y, _k)
            elbos.append(compute_elbo(a, b, nu, omega, x, y, a_0, b_0, mu_0).numpy()[0])

    return omega, nu, elbos

omega, nu, elbo = variational_inference(x, y, a_0, b_0, mu_0, k)
plt.plot(elbo);plt.title("ELBO by update")
plt.show()
plt.scatter(x_list, y.numpy())
plt.title("Actual: " + polynomial_str)
for i in range(50):
    betas = MN(nu, 1e-7 + torch.diag(1./omega)).sample().tolist()
    plt.plot(x_list_extr,polynomial(betas, np.array(x_list_extr)), alpha=0.05, color="blue")
plt.xlim(min(x_list_extr),max(x_list_extr))
VI_nu = nu.tolist()
print("VI:")
print(VI_nu)
print("MCMC (expectation): ")
print(MCMC_expectation)
print("Analytical: ")
print(analytical_inferred_mu)
plt.show()

def compute_stochastic_elbo(a, b, nu, omega, x, y, a_0, b_0, mu_0):
    """
    Return a monte-carlo estimate of the ELBO, using a single sample from Q(sigma^-2, beta)
    
    a, b are the Gamma 'shape' and 'rate' parameters for the variational posterior over *precision*: q(tau) = q(sigma^-2)
    nu_k, omega_k are Normal 'mean' and 'precision' parameters for the variational posterior over weights: q(beta_k)
    x is an n by k matrix, where each row contains the regression inputs [1, x, x^2, x^3]
    y is an n by 1 values
    a_0, b_0 the parameters for the Gamma prior over precision P(tau) = P(sigma^-2)
    mu_0 is the mean of the Gamma prior on weights beta
    """
    
    # Define mean field variational distribution over (beta, tau).
    Q_beta = Normal(nu, omega**-0.5)
    Q_tau = Gamma(a, b) 
    
    # Sample from variational distribution: (tau, beta) ~ Q
    # Use rsample to make sure that the result is differentiable.
    tau = Q_tau.rsample()
    sigma = tau**-0.5
    beta = Q_beta.rsample()
    
    # Create a single sample monte-carlo estimate of ELBO.
    P_tau = Gamma(a_0, b_0) 
    P_beta = Normal(mu_0, sigma) 
    P_y = Normal((beta[None, :]*x).sum(dim=1, keepdim=True), sigma) 
    
    kl_tau = Q_tau.log_prob(tau) - P_tau.log_prob(tau)
    kl_beta = Q_beta.log_prob(beta).sum() - P_beta.log_prob(beta).sum()
    log_likelihood = P_y.log_prob(y).sum()

    elbo = log_likelihood - kl_tau - kl_beta
    return elbo


def stochastic_gradient_variational_bayes(x, y, a_0, b_0, mu_0, k, n_iterations=20000):
    
    x = features(x,k)
    
    #We'll check that the elbo increases with each update
    elbos = []
    
    #initialize latent variables
    a = Parameter((k + 1. + len(y))/2. + a_0) #a does not get updated further
    b = Parameter(b_0.clone())
    omega = Parameter(Uniform(0.5, 1.5).sample(sample_shape=torch.Size([k])))
    nu = Parameter(Normal(0,1).sample(sample_shape=torch.Size([k])))
    
    optimizer = Adam([a, b, omega, nu], lr=1e-3)
    #start iterative updates
    for i in range(n_iterations):
        elbo = compute_stochastic_elbo(a*1, b*1, nu*1, omega*1, x, y, a_0, b_0, mu_0) #*1 is for making a Tensor
        elbos.append(elbo.item() if i==0 else 0.9*elbos[-1] + 0.1*elbo.item()) #Keep running average
        (-elbo).backward()
        optimizer.step()
        optimizer.zero_grad()
        if i%1000==0: print("Iteration", i, "ELBO", elbos[-1])
        
    return omega, nu, elbos


omega, nu, elbo = stochastic_gradient_variational_bayes(x, y, a_0, b_0, mu_0, k)
plt.plot(elbo)
plt.title("ELBO by update")
plt.show()
plt.scatter(x_list, y.numpy())
plt.title("Actual: " + polynomial_str)
for i in range(50):
    betas = MN(nu, 1e-7 + torch.diag(1./omega)).sample().tolist()
    plt.plot(x_list_extr,polynomial(betas, np.array(x_list_extr)), alpha=0.05, color="blue")
plt.xlim(min(x_list_extr),max(x_list_extr))
SGVB_nu = nu.tolist()
print("SGVB:")
print(SGVB_nu)
print("VI:")
print(VI_nu)
print("MCMC (expectation): ")
print(MCMC_expectation)
print("Analytical: ")
print(analytical_inferred_mu)
plt.show()