import matplotlib.pyplot as plt
import numpy as np

from scipy.special import factorial, gamma

"""
Grünwald-Letnikov (grunwaldletnikov grunwald letnikov) fractional derivative.
"""

# fractional order
eta = .8

# temporal domain and time step size
dt = 1e-3
tmax = 1
tmin = 0
steps = tmax/dt 

# Solve the fractional differential equation:
# d^eta f(t) /dt^eta = t^k
k = 2

# Analytical solution
fa = []
for i in range(tmin, tmax, dt)
    fa.append(gamma(k+1)/gamma(k+eta+1)*i**(k+eta))

plt(range(tmin, tmax, dt), fa)

# Grunwalk-Letnikov integration
c = np.zeros(steps)
c[0] = eta

for i in range(2, steps):
    c[i] = (1-(1+eta)/i)*c[i-1]

# Initialize solution.
f = np.zeros(steps)

for i in range(steps-1):
    f[i+1] = dt**eta*(t[i]**k) + c[1:i]*f[i:-1:1]

plt(range(tmin, tmax, dt), f)
plt.xlabel("time (A.U.)") 
plt.ylabel("f(t)")
