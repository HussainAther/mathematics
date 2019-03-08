import numpy as np

from fourier import *

"""
We can use the Fast Fourier transform to compute integrals of the form

integral from a to be of exp(i*omega*t) * h(t) * dt

which can be split up into real and imaginary parts

integral from a to be of cos(omega*t) * h(t) * dt and integral from a to be of sin(omega*t) * h(t) * dt
Taking advantage of hte oscillatory nature of the integral, if h(t) is at all smooth and omega is large
enough to imply several cycles in the interval [a, b], then the value of I is typically very small that it's sswamped
by the first-order error.

Given sampled points h_j, we approximate h(t) everywhere in the interval [a, b] by interpolation on nearby h_j's.

"""

