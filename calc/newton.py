from sys import version
import numpy as np

"""
Use Newton-Raphson method to find zero of a function.
"""

if int(version[0])>2: # Python 3 deprecated
    raw_input = input

x = 4 # starting point
dx = 3e-1 # differential step
eps = 0.2 # precision
imax = 100 # number of iterations

def f(x):
    """
    Some function.
    """
    return 2*np.cos(x) - x

for i in range(0, imax + 1):
    F = f(x)
    if abs(F) <= eps:
        print("Root found, precision eps = ", str(eps))
        break
    df = f(x + dx/2) - f(x-dx/2))/dx
    dx = -F/df
    x += dx

print("Enter and return any character to quit")
s = raw_input()
