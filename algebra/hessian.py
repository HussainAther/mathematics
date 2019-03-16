import numpy as np

"""
We can use backpropogation to evaluate the second derivates of the error, given by
the second derivate of the error with respect to weights. We use the element H_ij
of the Hessian matrix H in which i, j are included in the set {1,...W} in which W is the total
number of weights and biases.

1. Several nonlinear optimization algorithms used for training neural networks are based
on considerations of the second-order properties of the error surface, which are controlled
by the Hessian matrix (Bishop and Nabney, 2008).

2. The Hessian forms the basis of a fast procedure for re-training a feed-forward network
following a small change in the training data (Bishop, 1991).

3. The inverse of the Hessian has been used to identify the least significant weights in a
network as part of network ‘pruning’ algorithms (Le Cun et al., 1990).

4. The Hessian plays a central role in the Laplace approximation for a Bayesian neural network
(see Section 5.7). Its inverse is used to determine the predic- tive distribution for a trained network,
its eigenvalues determine the values of hyperparameters, and its determinant is used to evaluate
the model evidence.
"""

def hessian ( x, the_func, epsilon=1e-8):
    """Numerical approximation to the Hessian matrix
    x: array-like
        The evaluation point
    the_func: function
        The function. We assume that the function returns the function value and
        the associated gradient as the second return element
    epsilon: float
        The size of the step
    """

    N = x.size
    h = np.zeros((N,N))
    df_0 = the_func ( x )[1]
    for i in xrange(N):
        xx0 = 1.*x[i]
        x[i] = xx0 + epsilon
        df_1 = the_func ( x )[1]
        h[i,:] = (df_1 - df_0)/epsilon
        x[i] = xx0
    return h
