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

x = np.arange(-10, 10, 0.001)
p = norm.pdf(x, 0, 2)
q = norm.pdf(x, 2, 2)

plt.title("KL(P||Q) = %1.3f" % kl_divergence(p, q))
plt.plot(x, p)
plt.plot(x, q, c="red")
