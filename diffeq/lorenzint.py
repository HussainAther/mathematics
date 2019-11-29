import numpy as np

from ipywidgets import interact, interactive
from IPython.display import clear_output, display, HTML
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import cnames
from matplotlib import animation
from scipy import integrate

"""
Interactive animated Lorenz System of differential equations

dotx = 𝜎(y-x)
doty = 𝜌x-y-xz
dotz = -𝛽z+xy 
"""

def solve_lorenz(N=10, angle=0.0, max_time=4.0, sigma=10.0, beta=8./3, rho=28.0):
    """
    Solve the system of equations using scipy.
    """
    fig = plt.figure()
    ax = fig.add_axes([0, 0, 1, 1], projection='3d')
    ax.axis("off")

    # Prepare the axes limits
    ax.set_xlim((-25, 25))
    ax.set_ylim((-35, 35))
    ax.set_zlim((5, 55))

    def lorenz_deriv(x_y_z, t0, sigma=sigma, beta=beta, rho=rho):
        """
        Compute the time-derivative of a Lorenz system.
        """
        x, y, z = x_y_z
        return [sigma * (y - x), x * (rho - z) - y, x * y - beta * z]
