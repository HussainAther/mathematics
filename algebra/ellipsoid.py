import numpy as np

"""
Ellipsoid algorithm for linear programming uses the ellipsoid method to derive
the first polynomial time algorithm for linear programming. Theoretically better than
Simplex algorithm which has an exponential running time in its worst case.

A hyperplane is the set of points that satisfies the linear equation ax = b (where a, x, and b are ∈ R^n).
A convex set K is a set of points such that  ∀x, y ∈ K, λx+(1−λ)y ∈ K, where λ ∈ [0, 1]. A Convex Body is a closed and bounded
convex set.

"""

def ellipsoid(Eo, Vl):
    """
    With input bounding ellipsoid Eo for S and a lower bound Vl on Vol(S),
    output "yes" if the linear program is feasible and "no" otherwise.
    """
