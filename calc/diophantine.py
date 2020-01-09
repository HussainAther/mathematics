import numpy as np

"""
Diophantine (diophantine) equations solutions.
"""

def lineardio(a, b, c):
    """
    Solving linear ax + by = c.
    """
    q, r = divmod(a, b) # return the quotient and remainder of a / b
    if r == 0:
        return([0, c/b]) # solution
    sol = lineardio(b, r, c)
    u = sol[0]
    v = sol[1]
    return([v, u-q*v])

"""
Pell's equation (Pell Fermat Pell-Fermat) equation
"""

def func(a, b, c):
    """
    Function for an equation of this format with 
    coefficients a, b, and c. 
    """
    t = a[0]
    a[0] = b[0]
    b[0] = b[0]*c + t

def solvepell(n, a, b):
    """
    Solve the Pell equation with n, a, and b.
    """
    x = int(np.sqrt(n))
    y = x
    z = 1
    r = x << 1
    e1 = [1]
    e2 = [0]
    f1 = [0]
    f2 = [1]
    while True:
        y = r * z - y
        z = ((n - y * y) // z)
        r = (x + y) // z
        func(e1, e2, r)
        fun(f1, f2, r)
        a[0] = f2[0]
        b[0] = e2[0]
        fun(b, a, x)
        if a[0] * a[0] - n * b[0] * b[0] == 1:
            return
