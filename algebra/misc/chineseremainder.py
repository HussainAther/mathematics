from functools import reduce

"""
The Chinese remainder theorem is a theorem of number theory, which states that 
if one knows the remainders of the Euclidean division of an integer n by several 
integers, then one can determine uniquely the remainder of the division of n by 
the product of these integers, under the condition that the divisors are pairwise coprime.
"""

def chinese_remainder(n, a):
    """
    Chinese remainder theorem to determine
    the remainder of division of n by a in which
    n and a are both arrays of the numbers to use.
    """
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

def mul_inv(a, b):
    """
    Modular multiplicative inverse.
    """
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1 
