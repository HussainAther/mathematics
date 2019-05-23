"""
Greatest common divisor (gcd) Euclid's (euclid) algorithm.
"""

def gcd(a, b):
    """
    For two numbers a and b, find g such that g is a gcd of a and b.
    """
    if b == 0:
        return a
    else:
        return gcd(b, a % b)
