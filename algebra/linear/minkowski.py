from decimal import Decimal

"""
Minkowski distance in machine learning lets us find the distance similarity of a vector
in the context of two or more vectors.
"""

def rootdist(a, root):
    """
    Calculate distance value to a given root value.
    """
    rv = 1/float(root) # root value
    return round(Decimal(v) ** Decimal(rv),3)

def mink(x, y, p):
    """
    Return Minkowski (minkowski) distance for x, y, and a p-value p.
    Here the p-value should be reasonably low.
    """
    return p(sum(math(pow(abs(a-b), p) for a, b in zip(x, y)), p)) 
