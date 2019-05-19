import numpy as np
import autograd.numpy as np

from scipy.optimize import minimize
from autograd import grad

"""
We can find a point on a plane closest to the origin by minimizing a function along it.
This way we are constraining the problem to a certain condition. 
"""

def objective(X):
    """
    For a 3-member tuple X, define our objective function.
    """
    x, y, z = X
    return x**2 + y**2 + z**2

def eq(X):
    """
    Derivative of objective. Used in minimization.
    """
    x, y, z = X
    return 2 * x - y + z - 3

sol = minimize(objective, [1, -0.5, 0.5], constraints={"type": "eq", "fun": eq})

"""
Construct the constrained optimization problem using Lagrange multipliers.
Use an augmented unconstrained optimization problem with fsolve.
"""

def F(L):
    """
    Augmented Lagrange function, similar to the objective function above.
    """
    x, y, z, _lambda = L
    return objective([x, y, z]) - _lambda * eq([x, y, z])

# Gradients of the Lagrange function
dfdL = grad(F, 0)
