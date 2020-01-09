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
