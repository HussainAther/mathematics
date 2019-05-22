import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import numpy as np

from scipy.stats import norm
from sklearn.neighbors import KernelDensity
from sklearn.grid_search import GridSearchCV
from sklearn.cross_validation import LeaveOneOut

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
hist = plt.hist(x, bins=30, normed=True)
density, bins, patches = hist
widths = bins[1:] - bins[:-1]

# Effect of bin size 
x = make_data(20)
bins = np.linspace(-5, 10, 10)
fig, ax = plt.subplots(1, 2, figsize=(12, 4),
                       sharex=True, sharey=True,
                       subplot_kw={"xlim":(-4, 9),
                                   "ylim":(-0.02, 0.3)})
fig.subplots_adjust(wspace=0.05)
for i, offset in enumerate([0.0, 0.6]):
    ax[i].hist(x, bins=bins + offset, normed=True)
    ax[i].plot(x, np.full_like(x, -0.01), "|k",
               markeredgewidth=1)

# Use normal standard curve
x_d = np.linspace(-4, 8, 1000)
density = sum(norm(xi).pdf(x_d) for xi in x)

plt.fill_between(x_d, density, alpha=0.5)
plt.plot(x, np.full_like(x, -0.1), '|k', markeredgewidth=1)

plt.axis([-4, 8, -0.2, 5])

# instantiate and fit the kernel density estimation model
kde = KernelDensity(bandwidth=1.0, kernel="gaussian")
kde.fit(x[:, None])

# score_samples returns the log of the probability density
logprob = kde.score_samples(x_d[:, None])

plt.fill_between(x_d, np.exp(logprob), alpha=0.5)
plt.plot(x, np.full_like(x, -0.01), "|k", markeredgewidth=1)
plt.ylim(-0.02, 0.22)

# Selecting the bandwidth via cross-validation

bandwidths = 10 ** np.linspace(-1, 1, 100)
grid = GridSearchCV(KernelDensity(kernel="gaussian"),
                    {"bandwidth": bandwidths},
                    cv=LeaveOneOut(len(x)))
grid.fit(x[:, None])
