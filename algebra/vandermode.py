from vpython import *
import math

"""
Interpolation using the Vandermode function.

The Vandermonde matrix is an n × n matrix where the first row is the first point evaluated at
each of the n monomials, the second row is the second point x2 evaluated at each of the n monomials,
and so on.

The easiest way to create this matrix is to write the functions above the matrix and the points
to the left of the matrix as is shown below. Then evaluate the functions at the corresponding points.
"""
