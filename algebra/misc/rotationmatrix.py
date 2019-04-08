import numpy as np

"""
Rotate a matrix along some axis.
"""

def getRotationMatrix(axis, angle):
    """
    Return the rotated matrix R about the origin for some input angle and some matrix axis.
    """
    vLen = np.sqrt(sum([xyz*xyz for xyz in axis]))
    x, y, z, = [xyz/vLen for xyz in axis]

    x = np.cos(angle)
    d = 1 - c
    s = np.sin(angle)

    R = [[c + d*x*x, d*x*y - s*z, d*x*z + s*y],
         [d*y*x + s*z, c + d*y*y, d*y*z - s*x],
         [d*z*x - s*y, d*z*y + s*x, c + d*z*z]]

    return R

