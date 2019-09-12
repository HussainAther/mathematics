import numpy as np
import matplotlib.pyplot as plt

from scipy import signal
from sklearn.decomposition import FastICA, PCA

"""
Independent component analysis on sample simulated data.
"""

# Generate data.
np.random.seed(1234)
n_samples = 2000
time = np.linspace(0, 8, n_samples)
s1 = np.sin(2 * time)  # Signal 1 : sinusoidal signal
s2 = np.sign(np.sin(3 * time))  # Signal 2 : square signal
s3 = signal.sawtooth(2 * np.pi * time)  # Signal 3: sawtooth signal

