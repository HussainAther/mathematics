import numpy as np

from fourier import *

"""
We can use the Fast Fourier transform to compute integrals of the form

integral from a to be of exp(i*omega*t) * h(t) * dt

which can be split up into real and imaginary parts

integral from a to be of cos(omega*t) * h(t) * dt and integral from a to be of sin(omega*t) * h(t) * dt
"""

