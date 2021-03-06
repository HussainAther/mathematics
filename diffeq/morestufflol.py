import matplotlib.pyplot as plt
import numpy as np

from scipy.integrate import odeint # scipy has some neato ordinary differential equation functions.

"""
First-order differential equations.
"""

# Define a function which calculates the derivative.
def dy_dx(y, x):
    return x - y

xs = np.linspace(0,5,100)
y0 = 1.0  # the initial condition
ys = odeint(dy_dx, y0, xs)
ys = np.array(ys).flatten()

# Plot the numerical solution.
plt.rcParams.update({"font.size": 14})  # increase the font size
plt.xlabel("x")
plt.ylabel("y")
plt.plot(xs, ys);

y_exact = xs - 1 + 2*np.exp(-xs)
y_difference = ys - y_exact
plt.plot(xs, ys, xs, y_exact, "+");

y_diff = np.abs(y_exact - ys)
plt.semilogy(xs, y_diff)
plt.ylabel("Error")
plt.xlabel("x")
plt.title("Error in numerical integration")
