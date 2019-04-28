"""
The Neimarck-Sacker bifurcation is a closed invariant curve from a fixed point
in dynamical systems with discrete time when the fixed point changes stability
via a pair of complex eigenvalues with unit modulus. This is the Hopf
bifurcation equivalent for maps.

We observe a Neimark-Sacker bifurcation as either subcritical or supercritical 
by the sign of the first Lyapunov coefficient.
"""

def ns(d):
    """
    For a map in dictionary form d with a Jacobian matrix of the map
    such that this matrix has a pair of eigenvalues λ(a) = R(a)exp(i*θ(a))
    for d(a) over an interval of a-values of interest.
    """
    
