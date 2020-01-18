import matplotlib.pyplot as plt
import numpy as np

"""
Logistic map bifurcation
"""

def logistic(r, x):
    """
    Logistic map function for nonlinear systems
    """
    return r * x * (1 - x)

x = np.linspace(0, 1)
fig, ax = plt.subplots(1, 1)
ax.plot(x, logistic(2, x), "k")
