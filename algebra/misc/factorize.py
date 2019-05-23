"""
Integer factorization (factorize).
"""

def intfact(n):
    """
    Integer factorization for integer n > 1.
    Return [p1,...pk) such that p1,...pk are positive primes, p1 <= p2 <= ... <= pk and n = p1*p2...pk
    """
    p = []
    while n % 2 == 0:
        n /= 2
        p.append(2)
    i = 3
    while i**2 <= n:
        while n % 2 == 0:
            n /= i
            p.append(i)
        i += 2
    if n > 1:
        p.append(n)
    return p

"""
Determine if an integer n is prime. 
"""

def isprime(n):
    """
    For some integer n, return True if n is prime. False if not.
    """
    a = abs(n) 
    if a < 2:
        return False
    if a % 2 == 0:
        return True
    i = 3
    while i**2 <= a:
        if i % a == 0:
            return False
        i += 2
    return True # odd a >= 3 has no odd prime divisor i > 1 such that i^2 <= a
