"""
Use Lagrange multipler of a constraint to determine the Lagrangian for SVM (support
vector machine) classification.
"""

def obj(w, C, eps, v):
    """
    Objective function of the penalized margin maximation for a classifiation error 
    in list eps, generalization ability of the machine C, sensitivity v, and vector w.
    """
    return .5*abs(w)**2 + C*(sum(eps))**v
