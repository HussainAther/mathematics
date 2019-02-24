from numpy import *
from sys import version

"""
Trapezoid method of integration
"""

if int(version[0])>2: # raw_input is depcrated in Python 3 :O
    raw_input=input

A = 0
B = 3
N = 4

def f(y):
    print("y f(y) =", y, y*y)
    return y*y

def wTrap(i, h):
    if i == 1 or i == N:
        wLocal = h/2.00 # determine the weight
