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
