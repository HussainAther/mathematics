import numpy as np
import theano
import theano.sandbox.rng_mrg

from theano import function, shared
from theano import tensor as TT

"""
Dynamical approach to stochastic sampling based off physical systems that evolve with
Hamiltonian dynamics. In a Markov chain Monte Carlo simulation, we sample from a given 
probabilitry distribution. Hamiltonian dynamics uses the probabilistic simulation in the
form of a Hamiltonian system. Use theano matrices. 
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
    
def hmc(initial_pos, initial_vel, stepsize, n_steps, energy_fn):
    """
    Hybrid (or Hamiltonian) Monte Carlo with initial states (z, r) as we test potential states after
    leapfrog integration.
    """
    # compute velocity at time-step: t + stepsize//2
    initial_energy = energy_fn(initial_pos)
    dE_dpos = TT.grad(initial_energy.sum(), initial_pos)
    vel_half_step = initial_vel - 0.5 * stepsize * dE_dpos
    # compute position at time-step: t + stepsize
    pos_full_step = initial_pos + stepsize * vel_half_step
    # perform leapfrog updates: the scan op is used to repeatedly compute
    # vel(t + (m-1/2)*stepsize) and pos(t + m*stepsize) for m in [2,n_steps].
    (all_pos, all_vel), scan_updates = theano.scan(
        leapfrog,
        outputs_info=[
            dict(initial=pos_full_step),
            dict(initial=vel_half_step)],
        non_sequences=[stepsize],
        n_steps=n_steps - 1)
    final_pos = all_pos[-1]
    final_vel = all_vel[-1]
    # The last velocity returned by scan is vel(t +
    # (n_steps - 1 / 2) * stepsize) We therefore perform one more half-step
    # to return vel(t + n_steps * stepsize)
    energy = energy_fn(final_pos)
    final_vel = final_vel - 0.5 * stepsize * TT.grad(energy.sum(), final_pos)
    # return new proposal state
    return final_pos, final_vel

def liouville(z, r):
    """
    Liouville's Liouville theorem. For space of variables (z, r), as the region evolves
    under Hamiltonian dynamics, the shape may change but volume remains constant.
    """
    dzdt = (max(z)-min(z))/len(z)
    drdt = (max(r)-min(r))/len(r)
    return dzdt, drdt

def mha(energy_prev, energy_next, s_rng):
    """
    Metropolis-Hastings (metropolis hastings) accept or reject boolean.
    """
    ediff = energy_prev - energy_next
    return (TT.exp(ediff) - s_rng.uniform(size=energy_prev.shape)) >= 0

def sample(s_rng, positions, energy_fn, stepsize, n_steps):
    """
    Perform one step of Hybrid (Hamiltonian) Monte Carlo sampling. 
    """
    # end-snippet-1 start-snippet-2
    # sample random velocity
    initial_vel = s_rng.normal(size=positions.shape)
    # end-snippet-2 start-snippet-3
    # perform simulation of particles subject to Hamiltonian dynamics
    final_pos, final_vel = simulate_dynamics(
        initial_pos=positions,
        initial_vel=initial_vel,
        stepsize=stepsize,
        n_steps=n_steps,
        energy_fn=energy_fn
    )
    # end-snippet-3 start-snippet-4
    # accept/reject the proposed move based on the joint distribution
    accept = metropolis_hastings_accept(
        energy_prev=hamiltonian(positions, initial_vel, energy_fn),
        energy_next=hamiltonian(final_pos, final_vel, energy_fn),
        s_rng=s_rng
    )
    # end-snippet-4
    return accept, final_pos
