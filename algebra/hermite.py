"""
Hermite polynomials are a classical orthogonal polynomial sequence. In probability, they give
rise to the Edgeworth series. In combinatorics, they're an example of an Appell sequence. In numerical
analysis, they're a Gaussian quadrature. In physics, they're used in eigenstars of the quantum
harmonic oscillator. In systemsm ,theory, they're used with nonlinear operations on Gaussian noise.
In random matrix theory, they're used in Wigner-Dyson ensembles.
"""

hermitepolynomials = { # key is the number of the polynomial, and value is the polynomial
    

}


def recursiveHermite(x,n):
    """
    Recursive functino to calculate hermite polynomials.
    """
    if n==0:
        return 1
    elif n==1:
        return 2*x
    else:
        return 2*x*recursiveHermite(x,n-1)-2*(n-1)*recursiveHermite(x,n-2)
