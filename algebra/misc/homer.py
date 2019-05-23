"""
Homer's (homer) algorithm to evaluate a polynomial method.
"""

def evaluate(f, a):
    """
    For an array of polynomial coefficients f and a value a, return the
    polynomial evaluated at a. The coefficients should be given such that
    the index of the arraay corresponded to that power polynomial. For example,
    3x^2 + 1 would be [1, 0, 3]. 
    """
    if f == []:
        return 0
    result = f[-1] # begin with leading coefficient
    i = len(f) - 1 # number of times to iterate 
    while i >= 0:
        result = f[i] + a*result
        i -= 1
    return result
