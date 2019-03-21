import numpy as np

"""
We use the Backward Euler method for evaluating differential eqiations.
"""

def be(f, y0, x_vals, h):
    """
    Compute the Backawrd Euler method for a function f with initial condition y0,
    over values x_vals, with step size h.
    """

