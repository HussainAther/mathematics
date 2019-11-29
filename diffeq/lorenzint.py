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
