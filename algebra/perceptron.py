import numpy as np

"""
Rosenblatt's pecreptron is an example of a linear discriminant model.

It uses a two-class model with an input vector x transformed using a fixed nonlinear
transformation to give a feature vector phi(x) and create a generalized linear model
of the form

y(x) = f(w^T*phi(x))

with a nonlinear activation function f(.) with as a step function:

f(a) 1 when a >=0 and -1 when a < 0.
"""

def predict(row, weights):
    """
    Make predcitions by evaluating candidate weight values in stoachastic
    gradient descent. After the model is finalized we start making predictions on test data.
    """
    activation = weights[0]
    for i in range(len(row)-1):
        activation += weights[i + 1] * row[i]
    return 1.0 if activation >= 0.0 else 0.0

