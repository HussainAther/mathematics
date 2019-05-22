import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import numpy as np

"""
Kernel density estimation with histograms.
"""

def make_data(N, f=0.3, rseed=1):
    """
    Generate random data.
    """
    rand = np.random.RandomState(rseed)
    x = rand.randn(N)
    x[int(f * N):] += 5
    return x

x = make_data(1000)
