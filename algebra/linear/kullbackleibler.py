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

kl_divergence = tf.reduce_sum(
    tf.where(p == 0, tf.zeros(pdf.shape, tf.float64), p * tf.log(p / q))
)
optimizer = tf.train.GradientDescentOptimizer(learning_rate).minimize(kl_divergence)
Only after

with tf.Session() as sess:
    sess.run(init)
    
    history = []
    means = []
    variances = []
    
    for i in range(epochs):
        sess.run(optimizer, { p: pdf })
        
        if i % 10 == 0:
            history.append(sess.run(kl_divergence, { p: pdf }))
            means.append(sess.run(mu)[0])
            variances.append(sess.run(sigma)[0][0])
    
    for mean, variance in zip(means, variances):
        q_pdf = norm.pdf(x, mean, np.sqrt(variance))
        plt.plot(x, q_pdf.reshape(-1, 1), c='red')
plt.title('KL(P||Q) = %1.3f' % history[-1])
    plt.plot(x, p_pdf.reshape(-1, 1), linewidth=3)
    plt.show()
    
    plt.plot(history)
    plt.show()
    
    sess.close()
