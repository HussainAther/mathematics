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

def kochCurve(n):
    """
    List of points on a Koch curve of order n,
    starting at point ab, and ending at point xy.
    """
    def koch(n, abxy):
        """
        Use the Koch formula to get the points.
        """
