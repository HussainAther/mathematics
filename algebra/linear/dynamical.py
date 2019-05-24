import numpy as np

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
    return -np.random.normal(z) * np.exp(z)
