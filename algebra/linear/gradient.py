import numpy as np

"""
Gradient checking for an artificial neural network.
"""

def gradcheck(self, X, y_enc, w1, w2, epsilon, grad1, grad2):
    """
    Apply gradient checking to return the relative error between
    numerically approximated gradients and the backpropagated gradients. 
    """
