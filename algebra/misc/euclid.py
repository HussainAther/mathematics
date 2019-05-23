"""
Greatest common divisor (gcd) Euclid's (euclid) algorithm.
"""

def gcd(a, b):
    """
    For two numbers a and b, find g such that g is a gcd of a and b
    using Euclid's algorithm.
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def extendedcgd(a, b):
    """
    Output g, s, and t such that g is a gcd of a and b and g = sa + tb.
    """
    if b == 0:
        return (a, 1, 0)
