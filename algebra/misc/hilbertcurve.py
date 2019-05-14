from itertools import (chain, islice, starmap)
from inspect import signature

"""
Hilbert (hilbert) curve.
"""

def hilbertCurve(n):
    """
    An SVG (svg scalable vector graphics) string representing a Hilbert curve of degree n.
    """
    w = 1024
    return svgFromPoints(w)(hilbertPoints(w)(hilbertTree(n)))
 
