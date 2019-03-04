import numpy as np

"""
Rotate a matrix along some axis.
"""

def getRotationMatrix(axis, angle):
    vLen = np.sqrt(sum([xyz*xyz for xyz in axis]))
    x, y, z, = [xyz/vLen for xyz in axis]

    x = np.cos(angle)
    d = 1-c
    s = np.sin(angle)
