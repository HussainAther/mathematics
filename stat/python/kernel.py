import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import numpy as np

from mpl_toolkits.basemap import Basemap
from scipy.stats import norm
from sklearn.base import BaseEstimator, ClassifierMixin
from sklearn.datasets import fetch_species_distributions
from sklearn.datasets.species_distributions import construct_grids
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
grid.best_params_

"""
KDE (Kernel desnity estimation) on sphere.
"""

data = fetch_species_distributions()

# Get matrices/arrays of species IDs and locations
latlon = np.vstack([data.train["dd lat"],
                    data.train["dd long"]]).T
species = np.array([d.decode("ascii").startswith("micro")
                    for d in data.train["species"]], dtype="int")

xgrid, ygrid = construct_grids(data)

# Plot coastlines with basemap
m = Basemap(projection="cyl", resolution="c",
            llcrnrlat=ygrid.min(), urcrnrlat=ygrid.max(),
            llcrnrlon=xgrid.min(), urcrnrlon=xgrid.max())
m.drawmapboundary(fill_color="#DDEEFF")
m.fillcontinents(color="#FFEEDD")
m.drawcoastlines(color="gray", zorder=2)
m.drawcountries(color="gray", zorder=2)

# Plot locations
m.scatter(latlon[:, 1], latlon[:, 0], zorder=3,
          c=species, cmap="rainbow", latlon=True)

# Set up the data grid for the contour plot
X, Y = np.meshgrid(xgrid[::5], ygrid[::5][::-1])
land_reference = data.coverages[6][::5, ::5]
land_mask = (land_reference > -9999).ravel()
xy = np.vstack([Y.ravel(), X.ravel()]).T
xy = np.radians(xy[land_mask])

# Create two side-by-side plots
fig, ax = plt.subplots(1, 2)
fig.subplots_adjust(left=0.05, right=0.95, wspace=0.05)
species_names = ["Bradypus Variegatus", "Microryzomys Minutus"]
cmaps = ["Purples", "Reds"]

for i, axi in enumerate(ax):
    axi.set_title(species_names[i])
    # Plot coastlines with basemap
    m = Basemap(projection="cyl", llcrnrlat=Y.min(),
                urcrnrlat=Y.max(), llcrnrlon=X.min(),
                urcrnrlon=X.max(), resolution="c", ax=axi)
    m.drawmapboundary(fill_color="#DDEEFF")
    m.drawcoastlines()
    m.drawcountries()
    # Construct a spherical kernel density estimate of the distribution
    kde = KernelDensity(bandwidth=0.03, metric="haversine")
    kde.fit(np.radians(latlon[species == i]))
    # evaluate only on the land: -9999 indicates ocean
    Z = np.full(land_mask.shape[0], -9999.0)
    Z[land_mask] = np.exp(kde.score_samples(xy))
    Z = Z.reshape(X.shape)
    # Plot contours of the density
    levels = np.linspace(0, Z.max(), 25)
    axi.contourf(X, Y, Z, levels=levels, cmap=cmaps[i])

