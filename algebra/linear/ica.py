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
