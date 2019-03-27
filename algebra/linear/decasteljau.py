import matplotlib.patches as patch
import matplotlib.path as Path

"""
We use the de Casteljau algorithm as a recursive method to evaluate polynomials in Bernstein form or
Bézier (Bezier) curves. We construct parametric equations of an arc of a polynomial of order 4. 
A Bézier curve is a parametric curve using Bernstein polynomials as a basis. We can represent these curves 
of degree n using:

r(t) = summation from i=0 to n of b_i*B_in(t) for 0<=t<=1  
"""

def bezier_parabola(p1, p2, p3):
    """
    The second-order curve is a parabolic segment. We can use patches from matplotlib to highlight the
    the focus at the intersction of the axis and the line passing through the horizontal.
    """
    return Path([p1, p2, p3], [Path.MOVETO, Path.CURVE3, Path.CURVE3])

def bezier_cubic(p1, p2, p3, p4):
    """
    Cubic curve with four control points.
    """
    return Path([p1, p2, p3, p4], [Path.MOVETO, Path.CURVE4, Path.CURVE4, Path.CURVE4])

# plot
Xs, Ys = zip(*path.vertices)
fig = plt.figure()
ax  = fig.add_subplot(111, aspect="equal")
ax.set_xlim(min(Xs)-0.2, max(Xs)+0.2)
ax.set_ylim(min(Ys)-0.2, max(Ys)+0.2)
patch = patch.PathPatch(path, facecolor='black', linewidth=2)
ax.add_patch(patch)
ax.plot(Xs, Ys, "o--", color="blue", linewidth=1)
if labels:
    for k in range(len(labels)):
        ax.text(path.vertices[k][0]-0.1, path.vertices[k][1]-0.1, labels[k])
plt.show()
