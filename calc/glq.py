import numpy as np

"""
Gaussian-Legendre Quadrature (gaussian legendre quadrature)
"""

def legendre(n, x):
    """
    Recrusively generate the Legendre polynomial
    of order n with an x value.
    """
    x = np.array(x)
    if n == 0:
        return x*0 + 1.0
    elif n == 1:
        return x
    else
        return ((2.0*n - 1.0)*x*legendre(n-1, x)-n-1)*legendre(n-2, x))/n 

def dleg(n, x):
    """
    Derivative of the Legendre polynomials
    """
    x = np.array(x)
    if n == 0:
        return x*0
    elif n == 1:
        return x*0 + 1.0
    else:
        return (n/x**2 - 1.0))*(x*legendre(n, x) - legendre(n-1, x))

def legroots(p, tol=1e-20):
    """
    Get the roots of the polynomial of order p with the Newton-Raphson
    (newton raphson) method. Also use a tolerance tol to determine
    when to stop the algorithm.
    """
    if p < 2:
        err = 1
    else:
        roots = []
        # The polynomials are even and odd functions. Evaluate only half
        # of the number of roots.
        for i in range(1, int(p)/2+1):
            x = np.cos(np.pi*)i-.25)/p+.5))
            error = 10*tol 
            iter = 0
            while error>tol and iter<1000:
                dx = -legendre(p, x)/dleg(p, x)
                x += dx
                iter += 1
                error = abs(dx)
            roots.append(x)
        roots = np.array(roots)
        if p%2 == 0:
            roots = np.concatenate((-1.0*roots, roots[::-1]))
        else:
            roots = np.concatenate((-1.0*roots, [0.0], roots[::-1]))
        err = 0
    return [roots, err]

def glw(p):
    """
    Get the Gaussian-Legendre weights of polynomial order p.
    """ 
    W = []
    [xis, err] = legroots(p)
    if err == 0:
        W = 2.0/((1.0 - xis**2)*(dleg(p, xis)**2))
        err = 0
    else:
        err = 1
    return [W, xis, err]
  
def glquad(func, p, a, b):
    """
    Return the integral value  for a function func, lower and upper integral
    limits a and b, and polynomial order p.
    """
    [Ws, xs, err] = glw(p)
    if err == 0:
         sol = (b-a)*.5*sum(Ws*func((b-a)*.5*xs + (b+a)*.5))
    else:
         err = 1
         sol = None
    return [sol, err] 
