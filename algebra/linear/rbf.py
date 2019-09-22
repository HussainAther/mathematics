import numpy as np

def rbf(x, c, s):
    """
    Gaussian radial basis function (rbf) for neural networks. 
    """
    return np.exp(-1 / (2 * s**2) * (x-c)**2)

def kmeans(X, k):
    """
    K-means clustering for number of clusters k and array of inputs X.
    """
    # Randomly select initial clusters from input data.
    clusters = np.random.choice(np.squeeze(X), size=k)
    prevClusters = clusters.copy()
    stds = np.zeros(k)
    converged = False
    while not converged:
        distances = np.squeeze(np.abs(X[:, np.newaxis] - clusters[np.newaxis, :]))
        closestCluster = np.argmin(distances, axis=1)


