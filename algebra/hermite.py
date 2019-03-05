"""
Hermite polynomials are a classical orthogonal polynomial sequence. In probability, they give
rise to the Edgeworth series. In combinatorics, they're an example of an Appell sequence. In numerical
analysis, they're a Gaussian quadrature. In physics, they're used in eigenstars of the quantum
harmonic oscillator. In systemsm ,theory, they're used with nonlinear operations on Gaussian noise.
In random matrix theory, they're used in Wigner-Dyson ensembles.
"""

hermitepolynomials = { # key is the number of the polynomial, and value is the polynomial
    0: 1,
    1: x,
    2: x**2 - 1,
    3: x**3 - 3*x,
    4: x**4 - 6*x**2 + 3,
    5: x**5 - 10*x**3 + 15*x,
    6: x**6 - 15*x**4 + 45*x**2 - 15,
    7: x**7 - 21*x**5 + 105*x**3 - 105*x,
    8: x**8 - 28*x**4 + 210*x**4 - 420*x**2 + 105,
    9: x**9 - 36*x**7 + 378*x**5 - 1260*x**3 + 945*x,
    10: x**10 - 45*x**8 + 630*x**6 - 3150*x**4 + 4725*x**2 - 945
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
