from itertools import product

"""
Egyptian division is a method of dividing integers using addition and doubling that is similar to the algorithm 
of Ethiopian multiplication.

egyptian algorithm Algorithm 
"""

def egyptian_divmod(dividend, divisor):
    """
    Follow the rules with dividend and divisor
    """
    assert divisor != 0
    pwrs, dbls = [1], [divisor]
    while dbls[-1] <= dividend:
        pwrs.append(pwrs[-1] * 2)
        dbls.append(pwrs[-1] * divisor)
    ans, accum = 0, 0
    for pwr, dbl in zip(pwrs[-2::-1], dbls[-2::-1]):
        if accum + dbl <= dividend:
            accum += dbl
            ans += pwr
    return ans, abs(accum - dividend)
