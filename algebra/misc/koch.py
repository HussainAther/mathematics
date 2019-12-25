import numpy as np

from itertools import chain
from operator import add, sub

"""
Draw a Koch snowflake.
"""

def kochSnowflake(n, a, b):
    """
    List points on a Koch snowflake of order n from an equilateral
    triangle with bases a and b. 
    """
    points = [a, equilateralApex(a, b), b]
    return chain.from_iterable(
        map(kochCurve(n), points, points[1:] + [points[0]])
    )
