import numpy as np

from scipy.constants import golden
from scipy.integrate import quad

"""
Ergodicity have the property that "the time average equals the space average. This satisifies the ergodic hypothesis of thermodynamics. A process is ergodic if its time average is the same as its average over the probability space, known as the ensemble average. 
"""

# The golden angle is an irrational portion of a circle, 
# and so a sequence of rotations by the golden angle 
# will not repeat itself.
goldenangle = 2*np.pi*golden**-2

"""
If we picked a point x on a circle and rotated it repeatedly by a golden angle,
then we can use an integrable function f on the circle and form the average of its
values at the sequence of rotations. This is the time average.
"""

def T(x):
    """
    The ergodic transformation (rotating by the golden angle).
    """
    return (x + goldenangle) % (2*np.pi)

def timeaverage(x, f, T, n):
    """
    Integrate to get the time average.
    """
    s = 0
    for k in range(n):
        s += f(x)
        x = T(x)
    return s/n

"""
We can integrate f over the circle and divide by the circumference to get the space average.

The ergodic theorem says that the time average equals the space average, except possibly for a setting of starting values of measure zero.
"""

def spaceaverage(f):
    """
    Use scipy's built-in `quad` to integrate and get the space average.
    """
    integral = quad(f, 0, 2(np.pi)[0]
    return integral/(2*np.pi)

# Run it.
f = lambda x: np.cos(x)**2
N = 1e6

print(timeaverage(0, f, T, N))
print(spaceaverage(f))
