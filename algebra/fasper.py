import numpy as np

from fourier import *

"""
Fast computation of the Lomb Periodogram. We use the Fast Fourier transform to evluate
equations of the Lomb normalized periodogram. The fast algorithm makes feasible the application
of the Lomb method to data sets at least as large as 10^6 data points. It's faster than straightforward evaluation
of equations of Lomb normalized periodogram.
"""

