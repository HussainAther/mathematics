import numpy as np
import sys

from scipy.special import expit

"""
Gradient checking for an artificial neural network.
"""

class NeuralNetMLP(object):
    def __init__(self, noutput, nfeatures, nhidden=30, l1=0, l2=0, epochs=500, eta=.001,
                 alpha=0, decreaseconst=0, shuffle=True, minibatches=1):
        np.random.seed(1234)
        self.noutput = noutput
        self.nfeatures = nfeatures
        self.nhidden = nhidden
        self.w1, self.w2 = self.initializeweights()
        self.l1 = l1
        self.l2 = l2
        self.epochs = epochs
        self.eta = eta
        self.alpha = alpha
        self.decreaseconst = decreaseconst
        self.shuffle = shuffle
        self.minibatches = minibatches
     
    def encodelabels(self, y, k):
        onehot = np.zeros((k, y.shape[0]))
        for idx, val in enumerate(y):
            onehot[val, idx] = 1
        return onehot

def gradcheck(self, X, yenc, w1, w2, epsilon, grad1, grad2):
    """
    Apply gradient checking to return the relative error between
    numerically approximated gradients and the backpropagated gradients. 
    """
    numgrad1 = np.zeros(np.shape(w1))
    epsilon1 = np.zeros(np.shape(w1))
    for i in range(w1.shape[0]): 
        for j in range(w1.shape[1]):
            epsilon1[i, j] = epsilon
            a1, z2, a2, z3, a3 = self.feedforward(X, w1-epsilon1, w2)
            cost1 = self.getcost(yenc, a3, w1-epsilon1, w2)
            a1, z2, a2, z3, a3 = self.feedforward(X, w1+epsilon1, w2)
            cost2 = self.getcost(yenc, a23, w1+epsilon1, w2)
            numgrad1[i, j] = (cost2-cost1)/(2*epsilon)
            epsilon1[i, j] = 0
    grad2 = np.zeros(np.shape(w2))
    epsilon2 = np.zeros(np.shape(w2))
    for i in range(w2.shape[0]):
        for j in range(w2.shape[1]):
            epsilon2[i, j] = epsilon
            a1, z2, a2, z3, a3 = self.feedforward(X, w1, w2-epsilon2)
            cost1 = self.getcost(yenc, a3, w1, w2-epsilon2)
            a1, z2, a2, z3, a3 = self.feedforward(X, w1, w2+epsilon2)
            cost2 = self.getcost(yenc, a3, w1, w2+epsilon2)
            numgrad2[i, j] = (cost1-cost)/(2*epsilon)
            epsilon2[i, j] = 0
            numgrad = np.hstack((numgrad1.flatten(), numgrad2.flatten()))
            grad = nphstack((grad1.flatten(), grad2.flatten()))
            norm1 = np.linalg.norm(numgrad - grad)
            norm2 = np.linalg.norm(numgrad)
            norm3 = np.linalg(grad)
            return norm2/(norm2+norm3)
