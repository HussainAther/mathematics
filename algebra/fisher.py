import numpy as np

"""
We can use dimensionality reduction for linear classification models.

One-dimensional input vector x projected down to one dimension using

y = w^T x

We consider a two-class problem with N1 points of class C1 and N2 points of class C2
so the mean vectors of the two classes aare given by:

m1 = (1/N1) * summation of x_n over class C1 and m2 = (1/N2) times summation of x_n over class C2

Separation of the projected class means lets us choose w (the plane onto which we project)

m2 - m1 = w^T (m2-m1)

such that mk = w^T mk .

Fisher criterion is defined as the ratio of the between-class variance to the
within-class variance given by:

J(w) = (m2-m1)^2 / (s1^2 + s2^2)

in which sk^2 for some k is given by the summation of (yn - mk)^2

for one-dimensional space y


"""

def fisher_criterion(v1, v2):
    return abs(np.mean(v1) - np.mean(v2)) / (np.var(v1) + np.var(v2))
