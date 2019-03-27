import matplotlib.patches as patch
import matplotlib.path as Path

"""
We use the de Casteljau algorithm as a recursive method to evaluate polynomials in Bernstein form or
Bézier (Bezier) curves. We construct parametric equations of an arc of a polynomial of order 4. 
A Bézier curve is a parametric curve using Bernstein polynomials as a basis. We can represent these curves 
of degree n using:

r(t) = summation from i=0 to n of b_i*B_in(t) for 0<=t<=1  
"""

def bezier_parabola(P1, P2, P3):
    """
    The second-order curve is a parabolic segment. We can use patches from matplotlib to highlight the
    the focus at the intersction of the axis and the line passing through the horizontal.
    """
    return Path([P1, P2, P3], [Path.MOVETO, Path.CURVE3, Path.CURVE3])

def bezier_cubic(P1, P2, P3, P4):
    """
    Cubic curve with four control points.
    """
    return Path([P1, P2, P3, P4],
                [Path.MOVETO, Path.CURVE4, Path.CURVE4, Path.CURVE4])
