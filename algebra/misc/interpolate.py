"""
Let F = Q, R, C, or Z/(p), p prime (or indeed, let F be any field). Suppose we are given α1,...,αn,β1,...,βn ∈ F. Does there exist an f ∈ F[x] such that f(α1) = β1,...,f(αn) = βn? 
If so, can we calculate one of degree smaller than n?
"""

def interpolate(a, b):
    """
    For arrays a and b of the same length n, return a function f such that
    f(a1) = b1,...f(an) = bn and deg(f) < n.
    """
    x = 1
    i = 1
    f = b[0]
    while i < n:
        b = b*(x-a[i])
        i += 1
        f += (b[i] - f(a[i]))/a[i]) * b
    return f  
