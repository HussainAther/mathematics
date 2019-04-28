import numpy as np

"""
The Neimarck-Sacker bifurcation (NSB nsb) is a closed invariant curve from a fixed point
in dynamical systems with discrete time when the fixed point changes stability
via a pair of complex eigenvalues with unit modulus. This is the Hopf
bifurcation equivalent for maps.

We observe a Neimark-Sacker bifurcation as either subcritical or supercritical 
by the sign of the first Lyapunov coefficient.
"""

def theta(i):
    """
    Return theta for some angle i.
    """
    return np.sin(i)

def ns(d):
    """
    For a map in dictionary form d with a Jacobian matrix of the map
    such that this matrix has a pair of eigenvalues λ(a) = d(a)exp(i*θ(a))
    for d(a) over an interval of a-values of interest.
    """
    result = [] # NSB occurrences
    for key in d:
        if d[key] = 1 and theta(key) < np.pi and theta(key) > 0:
             result.append(key)
    # These results output hold true if the following non-degeneracy conditions hold:
    (1) dR/dd of (a) is != 0 and (2) exp(i*k*theta(a)) != 1 for k=1,2,3,4 
    return result 
