"""
A van der Corput (corput) sequence is one of the simplest one-dimensional 
low-discrepancy sequence over the unit interval. 
"""

def vdc(n, base=2):   
    """
    Given n, generates the nth term of the van der Corput sequence in base 2.
    """
    vdc, denom = 0,1
    while n:
        denom *= base
        n, remainder = divmod(n, base)
        vdc += remainder / denom
    return vdc
