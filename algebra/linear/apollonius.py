import numpy as np

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

    v11 = 2*x2 - 2*x1
    v12 = 2*y2 - 2*y1
    v13 = x1*x1 - x2*x2 + y1*y1 - y2*y2 - r1*r1 + r2*r2
    v14 = 2*s2*r2 - 2*s1*r1

    v21 = 2*x3 - 2*x2
    v22 = 2*y3 - 2*y2
    v23 = x2*x2 - x3*x3 + y2*y2 - y3*y3 - r2*r2 + r3*r3
    v24 = 2*s3*r3 - 2*s2*r2

    w12 = v12/v11
    w13 = v13/v11
    w14 = v14/v11

    w22 = v22/v21-w12
    w23 = v23/v21-w13
    w24 = v24/v21-w14

    P = -w23/w22
    Q = w24/w22
    M = -w12*P-w13
    N = w14 - w12*Q

    a = N*N + Q*Q - 1
    b = 2*M*N - 2*N*x1 + 2*P*Q - 2*Q*y1 + 2*s1*r1
    c = x1*x1 + M*M - 2*M*x1 + P*P + y1*y1 - 2*P*y1 - r1*r1 

    # Find a root of a quadratic equation. This requires the circle centers not to be e.g. colinear.
    D = b*b-4*a*c
    rs = (-b-np.sqrt(D))/(2*a)
 
    xs = M+N*rs
    ys = P+Q*rs

    return Circle(xs, ys, rs)
