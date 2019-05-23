from euclid import extendedcgd

"""
Let m and i be integers. Then [i]m is an invertible element of Z/(m) if and only if 1 is a gcd of m and i.

Determine if an element of Z/(m) is invertible, and if so, how to find its inverse.
"""

def inverse(i, m):
    """
    For integers i and m with m > 1, return t such that [t]_m = [i]_m^-1 if [i]_m is invertible.
    Return the empty sequence otherwise. 
    """
