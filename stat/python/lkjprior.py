import numpy as np
import pymc3 as pm
import seaborn as sns
import matplotlib.pyplot as plt

from matplotlib.patches import Ellipse

"""
LKJ Cholesky prior distribution. Use the inverse-Wishart distribution as the conjugate prior
for the covariance matrix of a multivariate normal distribution. Good for modeling
the covariance matrix of a multivariate normal distribution.
"""

np.random.seed(1234)

N = 10000
muactual = np.array([1, -2])
sigmaactual = np.array([[.5, -.3], [-.3, 1.]])
x = np.random.multivariate_normal(muactual, sigmaactual, size=N)
var, U = np.linalg.eig(sigmaactual)
angle = 180. / np.pi * np.arccos(np.abs(U[0, 0]))
fig, ax = plt.subplots(figsize=(8, 6))
blue, _, red, *_ = sns.color_palette()
e = Ellipse(muactual, 2 * np.sqrt(5.991 * var[0]),
            2 * np.sqrt(5.991 * var[1]),
            angle=angle)
e.set_alpha(0.5)
e.set_facecolor(blue)
e.set_zorder(10)
ax.add_artist(e)
ax.scatter(x[:, 0], x[:, 1], c="k", alpha=0.05, zorder=11)
rect = plt.Rectangle((0, 0), 1, 1, fc=blue, alpha=0.5)
ax.legend([rect], ["95% density region"], loc=2)

"""
Distribution density f(x | μ,Σ−1)=(2π)−k2|Σ|−12exp(−12(x−μ)⊤Σ−1(x−μ)).
The LKJ distribution provides a prior on the correlation matrix, C=Corr(xi,xj), 
which, combined with priors on the standard deviations of each component, induces 
a prior on the covariance matrix, Σ. Since inverting Σ is numerically unstable 
and inefficient, it is computationally advantageous to use the Cholesky decompositon 
of Σ, Σ=LL⊤, where L is a lower-triangular matrix. This decompositon allows 
computation of the term (x−μ)⊤Σ−1(x−μ) using back-substitution, which is more numerically 
stable and efficient than direct matrix inversion.
"""

with pm.Model() as model:
    packed_L = pm.LKJCholeskyCov("packed_L", n=2,
                                 eta=2., sd_dist=pm.HalfCauchy.dist(2.5))
