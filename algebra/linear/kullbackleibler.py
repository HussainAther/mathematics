import numpy as np
import tensorflow as tf
import seaborn as sns

from scipy.stats import norm
from matplotlib import pyplot as plt

sns.set()

"""
Kullback-Leibler (kullback leibler) divergence (kl).
"""

def kl_divergence(p, q):
    """
    Formula from Koch "Multivariate Analysis"
    """
    return np.sum(np.where(p != 0, p * np.log(p / q), 0))
