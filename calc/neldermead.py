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

def dh(f, xinit, s=.1, eps=1e-6):
    """
    Downhill simplex (Nelder-Mead) method for minimizing the user-supplied scalar function f(x)
    with respect to the vector x.
    xinit is the initial x vector.
    s is the side length of the simplex.
    eps (epsilon) is our tolerance.
    """
    n = len(xinit) # numbre of variables/dimensions
    x = np.zeros((n+1, n)) # initialize vector x array
    o = np.zeros(n+1) # initialize output array for our function f
    x[0] = xinit # initiialize simplex
    for i in range(1, n+1): # create the simplex
        x[i] = xinit
        x[i, i-1] = xinit[i-1] + s # account for multidimensional input vectors along the simplex
    for i in range(n+1):
        o[i] = f(x[i]) # evaluate our function and save to output array
    for k in range(500):
        ilo = np.argmin(f) # lowest vertex
        ihi = np.argmax(f) # highest vertex
        d = (-(n+1)*x[ihi] + np.sum(x, axis=0))/n # move vector d
        if np.sqrt(np.dot(d,d)/n) < eps:
            return x[ilo]
        xnew = x[ihi] + 2*d # reflection method
        fnew = f(xnew) # evaluate our function after reflecting the simplex
        if fnew <= f[ilo] # should we accept the reflection?


def nm():
    """
    """
    l = 1e6
    evalmin = .4
    a = np.array([[4.0*(x[0]**4 + x[1]**4), 2.0*x[1]**4], [2.0*x[1]**4, 4.0*x[1]**4]])
    b = np.array([[4.0*(x[0]**2 + x[1]**2), -3.0*x[1]**2], [-3*x[1]**2, 4.0*x[1]**2]])

