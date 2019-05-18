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
    For Lagrange multipliers alpha with x and y dictating parameters for the constraint,
    calculate dual Lagrangian.
    """
    return np.sum(alpha, axis = 0) - .5*(sum(sum(alpha*y*x.transpose(), sum=0), sum=1) 

"""
We can attain convex duality by subjecting the Lagrange multipler at the conditional minimization
of the objective function with our constraints. This gives the highest possible margin in the case 
in which classification errors are inevitable due to the linearity of the separating hyperplane.
We can calculate the Lagrangian functional for the primal problem. 
"""

def primalL(alpha, y, x, b, mu, w, C, eps):
    """
    For parameters alpha, y, x, b, mu, with vector w, generalization constant C, and error epsilon,
    calculate the Lagrange functional for the primal problem.
    """ 
    return .5*abs(w)**2 + C*(sum(eps)) - np.sum(alpha*(x.transpose()*w+b) -1 + eps, axis=0) - sum(mu*eps, axis=0)
