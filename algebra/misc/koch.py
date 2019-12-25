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
        (ab, xy) = abxy
        if n == 0:
            return [xy]
        else:
            (mp, mq) = midThirdOfLine(ab, xy)
            points = [ab, mp, equilateralaApex(mp, mq), mq, xy]
            return concatMap(curry(koch)(n - 1))(zip(points, points[1:])
    return lambda aab, xy: [ab] + koch(n, (ab, xy))

def equilateralApex(p, q):
    """
    Return the apex of a triangle with base p q.
    """
    return rotatedPoint(np.pi / 3)(p, q)

def rotatedPoint(theta):
    """
    Return the point ab rotated theta radins around the origin xy.
    """
