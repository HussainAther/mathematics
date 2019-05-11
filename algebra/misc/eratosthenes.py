import numpy as np

"""
The Sieve of Eratosthenes is an ancient algorithm to find all
prime numbers up to a limit.
"""

def erato(n):
    """
    For a given limit n, find the prime numbers up to it.
    """
    n = (n + 1) >> 1 # bit-wise operator for the limit
    p = np.ones(n, dtype=np.int8)
    i, j = 1, 3
    while i < n:
        if p[i]:
            p[j * j >> 1::j] = 0
        i, j = i+1, j+2
    return p.sum()
