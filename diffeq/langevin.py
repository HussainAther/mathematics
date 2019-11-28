import numpy as np
import matplotlib.pyplot as plt

"""
In stochastic differential equations we can model dynamical systems subject to noise for use
in physics, biology, and neuroscience. We will simlulate the Ornstein-Uhlenbeck process as a solution
of the Langevin (langevin) equation to describe the stochastic evolution of a particle in a fluid
under the influence of friction. We account for movement due ot collusions with the fluid (diffusion) 
and find the difference with the Brownian motion and friction. The Ornstein-Uhlenbeck process is
stationary, Gaussian, and Markov, so it can represent stationary random noise.

Langevin equation is:

dx = -((x-mu)/tau)dt + sigma * sqrt(2/tau) dW
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

fig, ax = plt.subplots(1, 1, figsize=(8, 4))
ax.plot(t, x, lw=2)

ntrials = 10000
X = np.zeros(ntrials)

# We create bins for the histograms.
bins = np.linspace(-2., 14., 100)
fig, ax = plt.subplots(1, 1, figsize=(8, 4))

for i in range(n):
    # Update the process independently for all trials.
    X += dt * (-(X - mu) / tau) + \
        sigma_bis * sqrtdt * np.random.randn(ntrials)
    # Display the histogram for a few points in time
    if i in (5, 50, 900):
        hist, _ = np.histogram(X, bins=bins)
        ax.plot((bins[1:] + bins[:-1]) / 2, hist,
                {5: '-', 50: '.', 900: '-.', }[i],
                label=f"t={i * dt:.2f}")
    ax.legend()

