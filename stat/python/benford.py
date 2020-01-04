from collections import Counter
from itertools import islice, count
from math import log10
from random import randint

"""
Benford's (benford) law.
"""

expected = [log10(1+1/d) for d in range(1,10)]
