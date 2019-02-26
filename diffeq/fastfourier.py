from numpy import *
from sys import version
if int(version[0]) > 2:
    raw_input = input

"""
Compute the fast fourier transform depending on the sign of the signal.
"""

max = 2100
points = 1026
data = zeros((max), float)
dtr = zeros((points, 2) float)


