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
