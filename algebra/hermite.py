import numpy as np
from numpy.polynomial.hermite import Hermite

"""
Hermite polynomials are a classical orthogonal polynomial sequence. In probability, they give
rise to the Edgeworth series. In combinatorics, they're an example of an Appell sequence. In numerical
analysis, they're a Gaussian quadrature. In physics, they're used in eigenstars of the quantum
harmonic oscillator. In systemsm ,theory, they're used with nonlinear operations on Gaussian noise.
In random matrix theory, they're used in Wigner-Dyson ensembles.

Hermite polynomials can be standardized for the "probabilists" using:

He_n(x) = (-1)^n * exp((x^2)/2 * d^n/dx*n(exp(-(x^2)/2)) = (x - d/dx)^n * 1

or for "physicists" using:

H_n(x) = (-1)^n * exp((x^2) * d^n/dx*n(exp(-(x^2))) = (2x - d/dx)^n * 1
"""

hpop = { # Hermite Probabilist's polynomials
        # key is the number of the polynomial, and value is the polynomial
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

hphp = {  # Hermite Physicist's polynomials
    0: 1,
    1: 2*x,
    2: 4*x**2 - 2,
    3: 8*x**3 - 12*x,
    4: 16*x**4 - 48*x**2 + 12,
    5: 32*x**5 - 160*x**3 + 120*x,
    6: 64*x**6 - 480*x**4 + 720*x**2- 120,
    7: 128*x**7 - 1344*x**5 + 3360*x**3 - 1680*x,
    8: 256*x**8 - 3584*x**6 + 13440*x**4 - 13440*x**2 + 1680,
    9: 512*x**9 - 9216*x**7 + 48384*x**5 - 80640*x**3 + 30240*x,
    10: 1024*x**10 - 23040*x**8 + 161280*x**6 - 403200*x**4 + 302400*x**2 - 30240,
}


def recursiveHermite(x,n):
    """
    Recursive function to calculate hermite polynomials.
    """
    if n==0:
        return 1
    elif n==1:
        return 2*x
    else:
        return 2*x*recursiveHermite(x,n-1)-2*(n-1)*recursiveHermite(x,n-2)


"""
The Hermite functions are a set of eigenfunctions of the continuous Fourier transform.
If we multiply the physicists version by exp((-1/2)*(x^2)), we get

exp((-1/2)*(x^2) + 2xt - t^2) summation from n=0 to infinity of exp((-1/2)*(x^2)) * H_n(x) * t^n/n! so that the left
"""

def hermiteFourier(x, n):
    """
    For a given x and n, calculate the left and right side of the Fourier transform dictated by
    the Hermite polynomials.
    """
    pass

"""
The solutions to the harmonic oscillator are Hermite polynomials.
Harmonic oscillator states are given by:

psi_n(x) = (1/sqrt(2^n * n)) * ((m*omega)/(pi*hbar))^(1/4) * exp((-m*omega*x^2)/(2*hbar)) * H_n(sqrt(m*omega/hbar)*x)

"""

def hoHermite(x,n,m,ohm):
    """
    Use Hermite polynomials to solve the Harmonic Oscillator.
    """
    vec = [0]*9
    vec[n] = 1
    Hn = Hermite(vec)
    return (1/sqrt(2**n*factorial(n)))*pow(m*ohm/pi,0.25)*exp(-0.5*m*ohm*x**2)*Hn(x*sqrt(m*ohm))
