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
