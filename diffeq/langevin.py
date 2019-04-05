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

dt = .001  # Time step.
T = 1.  # Total time.
n = int(T / dt)  # Number of time steps.
t = np.linspace(0., T, n)  # Vector of times.

sigma_bis = sigma * np.sqrt(2. / tau)
sqrtdt = np.sqrt(dt)

x = np.zeros(n)

for i in range(n - 1):
    """
    Simluate the process with the Euler-Maruyama method. It's the standard Euler method for ODOEs
    but with an extra stochastic term (scaled normal random variable).
    """
    x[i + 1] = x[i] + dt * (-(x[i] - mu) / tau) + sigma_bis * sqrtdt * np.random.randn()
