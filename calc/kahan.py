"""
Kahan (kahan) summation reduces numerical error in total we get from adding a sequence
of finite precision floating point numbers.
"""

def kahansum(l):
    """
    For a list of input numbers l, perform Kahan summation.
    """
    summ = c = 0
    for num in l:
        y = num - c
        t = summ + y
        c = (t - summ) - y
        summ = t
    return summ
