import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns; sns.set()

from matplotlib.image import imread
from mpl_toolkits import mplot3d
from sklearn.manifold import MDS, LocallyLinearEmbedding

"""
Manifold learning is a class of unsupervised estimators that seeks to describe datasets 
as low-dimensional manifolds embedded in high-dimensional spaces. When you think of a 
manifold, I"d suggest imagining a sheet of paper: this is a two-dimensional object that 
lives in our familiar three-dimensional world, and can be bent or rolled in that two 
dimensions. In the parlance of manifold learning, we can think of this sheet as a two-
dimensional manifold embedded in three-dimensional space.
"""

def make_hello(N=1000, rseed=42):
    """
    Make a plot with "HELLO" text; save as PNG.
    """
    fig, ax = plt.subplots(figsize=(4, 1))
    fig.subplots_adjust(left=0, right=1, bottom=0, top=1)
    ax.axis("off")
    ax.text(0.5, 0.4, "HELLO", va="center", ha="center", weight="bold", size=85)
    fig.savefig("hello.png")
    plt.close(fig)
    # Open this PNG and draw random points from it.
    data = imread("hello.png")[::-1, :, 0].T
    rng = np.random.RandomState(rseed)
    X = rng.rand(4 * N, 2)
    i, j = (X * data.shape).astype(int).T
    mask = (data[i, j] < 1)
    X = X[mask]
    X[:, 0] *= (data.shape[0] / data.shape[1])
    X = X[:N]
    return X[np.argsort(X[:, 0])]

X = make_hello(1000)
colorize = dict(c=X[:, 0], cmap=plt.cm.get_cmap("rainbow", 5))
plt.scatter(X[:, 0], X[:, 1], **colorize)
plt.axis("equal")

"""
Muldimensional scaling (MDS)
"""

def rotate(X, angle):
    """
    Rotate matrix X along angle.
    """
    theta = np.deg2rad(angle)
    R = [[np.cos(theta), np.sin(theta)],
         [-np.sin(theta), np.cos(theta)]]
    return np.dot(X, R)
    
X2 = rotate(X, 20) + 5
plt.scatter(X2[:, 0], X2[:, 1], **colorize)
plt.axis("equal")

model = MDS(n_components=2, dissimilarity="precomputed", random_state=1)
out = model.fit_transform(D)
plt.scatter(out[:, 0], out[:, 1], **colorize)
plt.axis("equal")

def random_projection(X, dimension=3, rseed=42):
    """
    Project randomly.
    """
    assert dimension >= X.shape[1]
    rng = np.random.RandomState(rseed)
    C = rng.randn(dimension, dimension)
    e, V = np.linalg.eigh(np.dot(C, C.T))
    return np.dot(X, V[:X.shape[1]])
   
X3 = random_projection(X, 3)
X3.shape 
ax = plt.axes(projection="3d")
ax.scatter3D(X3[:, 0], X3[:, 1], X3[:, 2],
             **colorize)
ax.view_init(azim=70, elev=50)

model = MDS(n_components=2, random_state=1)
out3 = model.fit_transform(X3)
plt.scatter(out3[:, 0], out3[:, 1], **colorize)
plt.axis("equal")

"""
Locally linear embedding.
"""

model = LocallyLinearEmbedding(n_neighbors=100, n_components=2, method="modified",
                               eigen_solver="dense")
out = model.fit_transform(XS)
fig, ax = plt.subplots()
ax.scatter(out[:, 0], out[:, 1], **colorize)
ax.set_ylim(0.15, -0.15)

