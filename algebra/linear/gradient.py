import numpy as np

"""
Gradient checking for an artificial neural network.
"""

def gradcheck(self, X, y_enc, w1, w2, epsilon, grad1, grad2):
    """
    Apply gradient checking to return the relative error between
    numerically approximated gradients and the backpropagated gradients. 
    """
    numgrad1 = np.zeros(np.shape(w1))
    epsilon1 = np.zeros(np.shape(w1))
    for i in range(w1.shape[0]): 
        for j in range(w1.shape[1]):
            epsilon1[i, j] = epsilon
            a1, z2, a2, z3, a3 = self.feedforward(X, w1 - epsilon1, w2)
