import numpy as np

from numpy.linalg import inv

"""
Kalman filter to determine velocity
of an aircraft.
"""

x_observations = np.array([4000, 4260, 4550, 4860, 5110])
v_observations = np.array([280, 282, 285, 286, 290])

z = np.c_[x_observations, v_observations]

# Initial Conditions
a = 2  # Acceleration
v = 280
t = 1  # Difference in time
