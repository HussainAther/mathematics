import numpy as np
from scipy.integrate import odeint

"""
We use the Lorenz system to discuss issues of dynamical systems. It illustrates non-linear systems theory and
chaos theory (like with the butterfly effect). We can simulate this.
"""

def Lorenz(s,t):
    """
    For three coupled differential equations with three state variables (indicated by the three-member s),
    we have three constants (sigma, rho, beta) to demonstrate chaotic behavior.
    """
    x = s[0]
    y = s[1]
    z = s[2]
  
    # constants for the equations
    sigma = 10.0
    rho = 28.0
    beta = 8.0/3.0
  
    # return the state derivatives
    return [sigma * (y-x), (rho-z)*x -y, x*y - beta*z]
