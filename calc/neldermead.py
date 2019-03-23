import numpy as np
import math

"""
We use the Nelder-Mead method (a.k.a downhill simplex, amoeba, or polytope method) to
find the minimum or maximum of an objective function in multidmensional space through
direct search. It's often used in nonlinear optimization problems for which derivatives
may not be known. It's a heuristic search method.

We examine a two-dimensinoal simplex (n=2) that

We use this method in requiring that the fundamental circular frequency of a stepped shaft which
is required to be higher than a certain value (w0). We determine the diameters d1 and d2
to minimize the volume of the material without violating the frequency constraint. The approximate
value of the fundamental frequency can be computed by solving the eigenvalue problem of
the two corresponding matrices.

D1 θ = c D2 θ

in which D1 and D2 are the two corresponding matrices for the distances
"""

def dh():
    """
    Downhill simplex (Nelder-Mead) method for minimizing the user-supplied scalar function f(x)
    with respect to the vector x.
    """

def nm():
    """
    """
    l = 1e6
    evalmin = .4
    a = np.array([[4.0*(x[0]**4 + x[1]**4), 2.0*x[1]**4], [2.0*x[1]**4, 4.0*x[1]**4]])
    b = np.array([[4.0*(x[0]**2 + x[1]**2), -3.0*x[1]**2], [-3*x[1]**2, 4.0*x[1]**2]])

