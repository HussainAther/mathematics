import numpy as np

from mpl_toolkits.mplot3d import Axes3D
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

# run the function on some sample data
state0 = [2.0, 3.0, 4.0]
t = arange(0.0, 30.0, 0.01)

state = odeint(Lorenz, state0, t)

# plot
fig = figure()
ax = fig.gca(projection="3d")
ax.plot(state[:,0], state[:,1], state[:,2])
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
show()
