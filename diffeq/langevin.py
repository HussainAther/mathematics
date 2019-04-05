import numpy as np
import matplotlib.pyplot as plt

"""
In stoachstic differential equations we can model dynamical systems subject to noise for use
in physics, biology, and neuroscience. We will simlulate the Ornstein-Uhlenbeck process as a solution
of the Langevin (langevin) equation to describe the stochastic evolution of a particle in a fluid
under the influence of friction. We account for movement due ot collusions with the fluid (diffusion) 
and find the difference with the Brownian motion and friction. The Ornstein-Uhlenbeck process is
stationary, Gaussian, and Markov, so it can represent stationary random noise.
"""

# Let's get Gaussian
sigma = 1 # standard deviation
mu = 20 # average
tau = .05 # time constant
