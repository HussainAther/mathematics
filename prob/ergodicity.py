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

"""
We can integrate f over the circle and divide by the circumference to get the space average.

The ergodic theorem says that the time average equals the space average, except possibly for a setting of starting values of measure zero.
"""
