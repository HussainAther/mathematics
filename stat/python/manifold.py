import matplotlib.pyplot as plt
import seaborn as sns; sns.set()
import numpy as np

"""
Manifold learning is a class of unsupervised estimators that seeks to describe datasets 
as low-dimensional manifolds embedded in high-dimensional spaces. When you think of a 
manifold, I'd suggest imagining a sheet of paper: this is a two-dimensional object that 
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
    # Open this PNG and draw random points from it
    from matplotlib.image import imread
    data = imread("hello.png")[::-1, :, 0].T
    rng = np.random.RandomState(rseed)
    X = rng.rand(4 * N, 2)
    i, j = (X * data.shape).astype(int).T
    mask = (data[i, j] < 1)
    X = X[mask]
    X[:, 0] *= (data.shape[0] / data.shape[1])
    X = X[:N]
    return X[np.argsort(X[:, 0])]
