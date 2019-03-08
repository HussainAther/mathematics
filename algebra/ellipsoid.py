import numpy as np

"""
Ellipsoid algorithm for linear programming uses the ellipsoid method to derive
the first polynomial time algorithm for linear programming. Theoretically better than
Simplex algorithm which has an exponential running time in its worst case.

A hyperplane is the set of points that satisfies the linear equation ax = b (where a, x, and b are ∈ R^n).
A convex set K is a set of points such that  ∀x, y ∈ K, λx+(1−λ)y ∈ K, where λ ∈ [0, 1]. A Convex Body is a closed and bounded
convex set.

We observe if K ⊆ Rn is a convex set and p ∈ Rn is a point, then one of the following holds:
(i) p ∈ K
(ii) there is a hyperplane that separates p from K

A polynomial time Separating Oracle for a convex set K is a procedure which given x, either tells that x ∈ K or returns a hyperplane
separating x from K. The procedure should run in polynomial time. Note that from the previous observation, such a plane is guaranteed to exist.

We optimize by reducing an objective function to a series of feasibility problems by doing the following.
We start with an estimate of the maximum value, co, and check for feasibility of the folloiwng system:

(transpose of c) * x >= co
A * x <= b
x >= 0
"""

def ellipsoid(Eo, Vl):
    """
    With input bounding ellipsoid Eo for S and a lower bound Vl on Vol(S),
    output "yes" if the linear program is feasible and "no" otherwise.
    """
