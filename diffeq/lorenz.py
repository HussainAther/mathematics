import numpy as np

from mpl_toolkits.mplot3d import Axes3D
from scipy.integrate import odeint

"""
We use the Lorenz system to discuss issues of dynamical systems. It illustrates non-linear systems theory and
chaos theory (like with the butterfly effect). We can simulate this.
"""

def Lorenz(s):
    """
    For three coupled differential equations with three state variables (indicated by the three-members),
    we have three constants (sigma, rho, beta) to demonstrate chaotic behavior.
    """
    x = s[0]
    y = s[1]
    z = s[2]
  
    # constants for the equations
    sigma = 10.0
    rho = 28.0
    beta = 8.0/3.0
  
    # Return the state derivatives.
    return [sigma * (y-x), (rho-z)*x -y, x*y - beta*z]

# Run the function on some sample data.
state0 = [2.0, 3.0, 4.0]
t = np.arange(0.0, 30.0, 0.01) # Use numpy's arange function for a .01 step interval

state = odeint(Lorenz, state0, t)

# Plot.
fig = figure()
ax = fig.gca(projection="3d")
ax.plot(state[:,0], state[:,1], state[:,2])
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
show()

"""
We can show how sensitive these equations are to initial conditions.
"""

t = np.arange(0.0, 30, 0.01)

state = [2.0001, 3.0, 4.0]
state = odeint(Lorenz, state2_0, t)

# animation
figure()
pb, = plot(state1[:,0],state1[:,1], "b-", alpha=0.2)
xlabel("x")
ylabel("y")

p = plot(state1[0:10,0], state1[0:10,1], "b-'"
pp = plot(state1[10,0], state1[10,1], "b.", markersize=10)
p2 = plot(state2[0:10,0], state2[0:10,1], "r-")
pp2 = plot(state2[10,0], state2[10,1], "r.", markersize=10)
tt = title("%4.2f sec" % 0.00)

# Animate.
step = 3
for i in xrange(1,shape(state1)[0]-10,step):
    p.set_xdata(state1[10+i:20+i,0])
    p.set_ydata(state1[10+i:20+i,1])
    pp.set_xdata(state1[19+i,0])
    pp.set_ydata(state1[19+i,1])
    p2.set_xdata(state2[10+i:20+i,0])
    p2.set_ydata(state2[10+i:20+i,1])
    pp2.set_xdata(state2[19+i,0])
    pp2.set_ydata(state2[19+i,1])
    tt.set_text("%4.2f sec" % (i*0.01))
    draw()

