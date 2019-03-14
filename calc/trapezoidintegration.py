from numpy import *
from sys import version

"""
Trapezoid method of integration. The trapezoid rule stakes each integration interval i and
constructs a trapezoid of width h in it. This approximates the function by a straight line in each
interval i and uses the average height as the value for f. The area is computed as the integral of
the function.
"""

if int(version[0])>2: # raw_input is depcrated in Python 3 :O
    raw_input=input

# define some constants
A = 0
B = 3
N = 4

def f(y):
    """
    Some function
    """
    print("y f(y) =", y, y*y)
    return y*y

def wTrap(i, h):
    if i == 1 or i == N:
        wLocal = h/2.00 # determine the weight. We can call it the local weight
    else:
        wLocal = h
    return wLocal

h = (B-A)/(N-1)
suma = 0

for i in range(1, N+1):
    t = A+(i-1)*h
    w = wTrap(i, h)
    suma = suma + w * f(t)

print("Total sum = ", suma)
print("Enter adn retrun any character to quit")
s = raw_input()
