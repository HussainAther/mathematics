import numpy as np
import matplotlib.pyplot as plt

from scipy.integrate import odeint

"""
Predator-Prey Equations

Also known as Lotka-Volterra equations, the predator-prey equations are a pair of first-order
nonlinear ordinary differential equations. They represent a simplified model of the change in
populations of two species which interact via predation. For example, foxes (predators) and rabbits
(prey). Let  x  and  y represent rabbit and fox populations, respectively. Then

dxdt=x(a−by) dydt=−y(c−dx)

Here  a ,  b ,  c  and  d  are positive parameters.
"""

a,b,c,d = 1,1,1,1

def dP_dt(P, t):
    """
    Differential form of the equation.
    """
    return [P[0]*(a - b*P[1]), -P[1]*(c - d*P[0])]

ts = np.linspace(0, 12, 100)
P0 = [1.5, 1.0]
Ps = odeint(dP_dt, P0, ts)
prey = Ps[:,0]
predators = Ps[:,1]

plt.plot(ts, prey, "+", label="Rabbits")
plt.plot(ts, predators, "x", label="Foxes")
plt.xlabel("Time")
plt.ylabel("Population")
plt.legend();

plt.plot(prey, predators, "-")
plt.xlabel("Rabbits")
plt.ylabel("Foxes")
plt.title("Rabbits vs Foxes");


ic = np.linspace(1.0, 3.0, 21)
for r in ic:
    P0 = [r, 1.0]
    Ps = odeint(dP_dt, P0, ts)
    plt.plot(Ps[:,0], Ps[:,1], "-")
plt.xlabel("Rabbits")
plt.ylabel("Foxes")
plt.title("Rabbits vs Foxes");
