import math

from collections import namedtuple

"""
Problem of Apollonius
Find one or more circles that are tangent to three 
given objects in a plane, where an object may be a 
line, a point or a circle of any size.
"""

Circle = namedtuple("Circle", "x, y, r")

def solveApollonius(c1, c2, c3, s1, s2, s3):
    """
    Find an algebraic solution by setting the 
    equations describing the circles equal to one another.
    """
    x1, y1, r1 = c1
    x2, y2, r2 = c2
    x3, y3, r3 = c3
