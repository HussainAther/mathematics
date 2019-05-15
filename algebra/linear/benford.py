from itertools import islice, count
from collections import Counter
from math import log10
from random import randint

"""
Benford's (Benford benford) law refers to the frequency distribution of digits in many real-life sources of data.

Calculate the distribution of first significant (non-zero) digits in a collection of numbers, then display the 
actual vs. expected distribution against the Fibonacci (fibonacci) sequence.
"""

expected = [log10(1+1/d) for d in range(1,10)]

def fib():
    """
    Fibonacci sequence
    """
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a+b

def power_of_threes():
    """
    Powers of three as a test sequence
    """
    return (3**k for k in count(0))

def heads(s):
    """
    Yield the first entry for each in s.
    """
    for a in s: yield int(str(a)[0])

def show_dist(title, s):
    """
    Show the distribution for a title and s.
    """
    c = Counter(s)
    size = sum(c.values())
    res = [c[d]/size for d in range(1,10)]
    print("\n%s Benfords deviation" % title)
    for r, e in zip(res, expected):
        print("%5.1f%% %5.1f%%  %5.1f%%" % (r*100., e*100., abs(r - e)*100.)) 

def rand1000():
    """
    Show a random integer up to 9999.
    """
    while True: yield randint(1,9999)

if __name__ == "__main__":
    show_dist("fibbed", islice(heads(fib()), 1000)) # for the Fibonnaci sequence
    show_dist("threes", islice(heads(power_of_threes()), 1000)) # for Benford's law
    show_dist("random", islice(heads(rand1000()), 10000)) # just to show that not all kind-of-random sets behave like that
