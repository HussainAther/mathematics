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

def wrap_function(function, args):
    """
    Wrap the function to get its calls.
    """
    ncalls = [0]
    if function is None:
        return ncalls, None

    def function_wrapper(*wrapper_args):
        ncalls[0] += 1
        return function(*(wrapper_args + args))

    return ncalls, function_wrapper

def minerror(centers, observ):
    """
    Minimize error given cluster centers and observations (observ)
    Use the BFGS algorithm. Broyden–Fletcher–Goldfarb–Shanno (BFGS) 
    algorithm.
    """
    minerror = np.inf
    f = observ
    fprime = None
    epsilon = .01
    x0 = asarray(x0).flatten()
    if x0.ndim == 0:
        x0.shape = (1,)
    if maxiter is None:
        maxiter = len(x0) * 200
    func_calls, f = wrap_function(f, args) 
    
    old_fval = f(x0)

    if fprime is None:
        grad_calls, myfprime = wrap_function(approx_fprime, (f, epsilon))
    else:
        grad_calls, myfprime = wrap_function(fprime, args)
    gfk = myfprime(x0)
    k = 0
    N = len(x0)
    I = numpy.eye(N, dtype=int)
    Hk = I
