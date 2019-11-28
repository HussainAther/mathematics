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

# Solve the fractional differential equation:
# d^eta f(t) /dt^eta = t^k
k = 2

# Analytical solution
fa = gamma(k+1)/gamma(k+eta+1)*t**(k+eta)
 
