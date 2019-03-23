import numpy as np

"""
We use the Nelder-Mead method (a.k.a downhill simplex, amoeba, or polytope method) to
find the minimum or maximum of an objective function in multidmensional space through
direct search. It's often used in nonlinear optimization problems for which derivatives
may not be known. It's a heuristic search method.

We use this method in requiring that the fundamental circular frequency of a stepped shaft which
is required to be higher than a certain value (w0). We determine the diameters d1 and d2
to minimize the volume of the material without violating the frequency constraint. The approximate
value of the fundamental frequency can be computed by solving the eigenvalue problem of
the two corresponding matrices.


"""

def nm():
    """
    """
    l = 1e6
    evalmin = .4
    a = np.array([[4.0*(x[0]**4 + x[1]**4), 2.0*x[1]**4], [2.0*x[1]**4, 4.0*x[1]**4]])
    b = np.array([[4.0*(x[0]**2 + x[1]**2), -3.0*x[1]**2], [-3*x[1]**2, 4.0*x[1]**2]])

