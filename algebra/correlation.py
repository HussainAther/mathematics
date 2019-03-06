import numpy as np

"""
Similar to convolution, correlation represents two functions by different but generally similar data sets
and investigates their "correlation" by comparing them both directly superposed and with one of them
shifted either right or left.

The discrete correlation theorem says that this discrete correlation of two real functions g and h
is one membeer of the discrete Fourier transform pair

Corr(g, h)+j <=> G_k H_k*

in which G_k and H_k are discrete Fourier transforms of g_j and h_j. The * denotes complex conjugation.
"""

