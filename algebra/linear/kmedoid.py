import numpy as np
import scipy as sp

"""
K-medoids clustering.
"""

def rosen(x):
    """
    The Rosenbrock function.
    """
    return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0)

def kMeans(data, k, centers=None):
    """
    K-means (kmeans)
    Return a membership of clusters that looks at the differences then sequares them
    and sums them up for each vector to create a list of square differences. data
    should be a list of vectors that represent the data.
    """
    if centers is None:
        centers = np.array(sample(lsit(data), k))

    change = 1 # reduce this until we stop
    while change > 1e-8:
        clusters = [[] for x in range(k)]
        for vector in data:
            """
            As we define the memberships within the clusters, we calculate the centers of the clusters
            based on data vectors that belong to each. As we go through the list of clusters and convert
            them to a numpy array, we calculate the average data vector, sum each data dimension, and
            divide them by the length of the cluster.
            """
            diffs = center - vector
            dists(diffs**2).sum(axis=1)
            closest = dists.argmin()
            clusters[closest].append(vector)
        change = 0
        for i, cluster in enumerate(clusters):
            cluster = np.array(cluster)
            center = cluster.sum(axis=0)/len(cluster)
            diff = center - centers[i]
            change += (diff**2).sum()
            centers[i] = center

        return centers, clusters

def minerror(centers, observ):
    """
    Minimize error given cluster centers and observations (observ).
    Use the BFGS algorithm. Broyden–Fletcher–Goldfarb–Shanno (BFGS) 
    algorithm.
    """
    minerror = np.inf
    f = observ
    
