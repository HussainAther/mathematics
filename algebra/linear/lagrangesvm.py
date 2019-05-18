import numpy as np

"""
Lagrangiann for SVM (support vector machine) classification.
"""

def obj(w, C, eps, v):
    """
    Objective function of the penalized margin maximation for a classifiation error 
    in list eps, generalization ability of the machine C, sensitivity v, and vector w.
    """
    return .5*abs(w)**2 + C*(sum(eps))**v

"""
We use three inequalities for all n points of the training set

xi^T w + b >= 1 - epsi for yi = 1
xi^T w + b <= -1 + epsi for yi = -1
epsi >= 0

which we combine to make the two constraints

yi(xi^T w + b) >= 1 - epsi
epsi >= 0

Using the Karush-Kuhn-Tucker conditions, we derive the dual Lagrangian
"""

def dualL(alpha, y, x):
    """
    For Lagrange multipliers alpha with x and y dictating parameters for the constraint.
    """

"""
We can attain convex duality by subjecting the Lagrange multipler
"""

