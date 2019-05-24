import numpy as np
import theano
import theano.sandbox.rng_mrg

from theano import function, shared
from theano import tensor as TT

"""
Dynamical approach to stochastic sampling based off physical systems that evolve with
Hamiltonian dynamics. In a Markov chain Monte Carlo simulation, we sample from a given 
probabilitry distribution. Hamiltonian dynamics uses the probabilistic simulation in the
form of a Hamiltonian system. 
"""

def K(r):
    """
    Kinetic energy for intermediate momentunm variables r, which correspond
    to change of state rate of state variablse z such that r = dz/dt.
    """
    summ = 0
    for i in r:
        summ += i ** 2
    return summ/2

def E(z):
    """
    Potential energy of a system for state variables z and probability
    distribution p. For this example, we assume the probability distribution
    is Gaussian (normal). 	
    """
    summ = 0
    for i in z:
        summ += -np.random.normal(z) * np.exp(z)
    return summ 

def H(z, r):
    """
    Hamiltonian, total, energy.
    """
    return E(z) + K(r)

"""
Hybrid Monte Carlo combines Hamiltonian dynamics with Metropolis algorithm to remove
any bias with discretization. It uses a Markov chain of alternate stochastic updates
of momentum variable r and Hamiltonian dynamical updates using the leapfrog algorithm.
"""

def logprob(x, ivar):
    """
    Logarithmic probability distribution.
    """
    logp = -0.5 * np.sum(ivar * x**2)
    grad = -ivar * x
    return logp, grad

def leapfrog(pos, vel, step):
    """
    Leapfrog update using Hamiltonian dynamics.
    """
    # from pos(t) and vel(t-stepsize//2), compute vel(t+stepsize//2)
    dE_dpos = TT.grad(energy_fn(pos).sum(), pos)
    new_vel = vel - step * dE_dpos
    # from vel(t+stepsize//2) compute pos(t+stepsize)
    new_pos = pos + step * new_vel
    return [new_pos, new_vel], {}
    
def hmc(z, r):
    """
    Hybrid (or Hamiltonian) Monte Carlo with initial states (z, r) as we test potential states after
    leapfrog integration.
    """
    minn = 0 
    zs = z[0] # z*
    if min(1, exp(H(z, r)

def liouville(z, r):
    """
    Liouville's Liouville theorem. For space of variables (z, r), as the region evolves
    under Hamiltonian dynamics, the shape may change but volume remains constant.
    """
    dzdt = (max(z)-min(z))/len(z)
    drdt = (max(r)-min(r))/len(r)
    return dzdt, drdt
