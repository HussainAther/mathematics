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

The Ellipsoid Algorithm solves the feasibility problem in an ingenious way. Let us denote the convex set
defined by the feasible solution space by S. Further, we assume that the constraints are non-degenerate,
so that S is either empty or has a non-zero volumed denoted by V ol(S). In other words we can find a lower
bound Vl on V ol(S). We start off with an ellipsoid of volume Vu guaranteed to bound S if it is finite.

If V ol(S) is infinite, we start with a suitable Vu and we will eventually get to a feasible point anyway.
In our case, the initial bounding ellipsoid is a sphere in Rn. A single step of the algorithm either
finds a point in S, in which case we have proved feasibility, or finds another ellipsoid bounding S that has
a volume that is substantially smaller than the volume of the previous ellipsoid.

We iterate on this new ellipsoid. In the worst case we need to iterate until the volume of the bounding ellipsoid
gets below Vl, in which case we can conclude that the system is infeasible. It turns out that only a polynomial number
of iterations are required in the case of linear programming. The algorithm does not require an explicit description
of the linear program. All that is required is a polynomial time Separating Oracle, which checks whether a point lies
in S or not, and returns a separating hyperplane in the latter case. The following high level pseudocode describes the algorithm
"""

def volEllipsoid(x, y, z):
    """
    With x, y, and z being the height, length, and width of the ellipsoid, return the volume.
    """
    return (4/3)*x*y*z

def sepOracle(p):
    """
    Check whether p satisfies the constraints of the linear program.
    Return ans as True or False.
    Return a violating constraint as H if it exists.
    """
    H = (0, 0, 0)
    ans = True
    return ans, H

def hyperplane(E, H):
    """
    Return the minimum volume ellipsoid containing the intersection of
    E and H. Do this by taking the separating hyperplane and calculating volume.
    
    Still working on this.
    """
    return E*H

def ellipsoid(Eo, Vl):
    """
    With input bounding ellipsoid Eo (in x, y, and z coordinates for
    height, length, and width centered at the origin) for S and a
    lower bound Vl on Vol(S), output True if the linear program is feasible and False otherwise.
    """
    i = 0
    while (volEllipsoid(Eo)> Vol):
        p = (0, 0, 0)
        (ans, H) = sepOracle(p)
        if ans == True:
            return True
        else:
            Eo = hyperplane(E, H)
    return False
