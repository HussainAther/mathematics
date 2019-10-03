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

"""
Minimize it.
"""

x = np.arange(-10, 10, 0.001)
p_pdf = norm.pdf(x, 0, 2).reshape(1, -1)
np.random.seed(0)
random_mean = np.random.randint(10, size=1)
random_sigma = np.random.randint(10, size=1)
random_pdf = norm.pdf(x, random_mean, random_sigma).reshape(1, -1)
learning_rate = 0.001
epochs = 100
p = tf.placeholder(tf.float64, shape=pdf.shape)
mu = tf.Variable(np.zeros(1))
sigma = tf.Variable(np.eye(1))
normal = tf.exp(-tf.square(x - mu) / (2 * sigma))
q = normal / tf.reduce_sum(normal)
