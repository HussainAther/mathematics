from collections import Counter
from itertools import islice, count
from math import log10
from random import randint

"""
Benford's (benford) law.
"""

expected = [log10(1+1/d) for d in range(1,10)]

def fib():
    """
    Fibnoacci sequence
    """
    a,b = 1,1
    while True:
        yield a
        a,b = b,a+b

def power_of_threes():
    """
    Powers of 3 
    """
    return (3**k for k in count(0))
 
def heads(s):
    """
    Header of the distribution
    """
    for a in s: yield int(str(a)[0])
