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
    return Path([P1, P2, P3], [Path.MOVETO, Path.CURVE3, Path.CURVE3])
