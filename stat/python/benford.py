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

def powerofthrees():
    """
    Powers of 3 
    """
    return (3**k for k in count(0))
 
def heads(s):
    """
    Header of the distribution
    """
    for a in s: yield int(str(a)[0])

def showdist(title, s):
    """
    Show the distribution.
    """
    c = Counter(s)
    size = sum(c.values())
    res = [c[d]/size for d in range(1,10)]
 
    print("\n%s Benfords deviation" % title)
    for r, e in zip(res, expected):
        print("%5.1f%% %5.1f%%  %5.1f%%" % (r*100., e*100., abs(r - e)*100.))

showdist("fibbed", islice(heads(fib()), 1000))
showdist("threes", islice(heads(powerofthrees()), 1000))
