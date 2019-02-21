import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind, ttest_1samp, poisson

"""
Simple statistics and methods to quantify uncertainty
"""

# Make up some data I don't know
# N = 25
N = 75
mu1 = 7
mu2 = 10
sd = 5

# Generate random data
data1 = sd * np.random.randn(N) + mu1
data2 = sd * np.random.randn(N) + mu2

# Histograms lol
fig, ax = plt.subplots()
ax.hist(data1)
ax.hist(data2)
