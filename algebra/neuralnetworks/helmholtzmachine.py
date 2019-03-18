import numpy as np

"""
The Helmholtz machine was designed to accommodate hierarchical architectures that construct complex
multilayer representations. The model in- volves two interacting networks, one with parameters G
that is driven in the top-down direction to implement the generative model, and the other, with
parameters W , driven bottom-up to implement the recognition model.

It uses a cycle between waking and sleeping (as part of the Wake-Sleep algorithm) in which a stochastic
multilayer neural network adjusts its own parameters to produce a good density estimator.

The parameters are determined by a modified EM algorithm that results in roughly symmetric updates for the two networks.
"""

def sigmoid(u):
    """
    A vectorized version of the logistic sigmoid firing function.
    """
    return 1/(1 + np.exp(np.negative(u)))

def bernoulliSample(probs):
    """
    Generate a binary vector according to a vector of probabilities.
    """
    return map( (lambda p : np.random.choice( (1.0,0.0), p=(p,1-p) )), probs )

def intToPattern(i, n):
    """
    An length n tuple of 0.,1.'s corresponding to the binary form of i.
    """
    return tuple(map(float, bin(i)[2:].zfill(n)))

def patternToString(d, c):
    """
    For prettyprinting a real binary pattern list in space-separated clumps (c).
    """
    s= ""
    for k in range(len(d)):
        if k%c == 0:
            s+= " "
        s += "1" if d[k]>0 else "0"
    return s

class HelmholtzMachine:
    def __init__(self, nTop, nMid, nBottom):
        """
        Construct a 3-layer HM with the given number of neurons at each level.
        """
        # Dimension of pattern vector visible at the bottom.
        self.dimension= nBottom

        # Generative weights (top down)
        self.bG= np.zeros(nTop)
        self.wG= np.zeros([nMid, nTop+1])
        self.vG= np.zeros([nBottom, nMid+1])
        
        # Recognition weights (bottom up)
        self.vR= np.zeros([nMid, nBottom+1])
        self.wR= np.zeros([nTop, nMid+1])
        
        # Some default learning rates
        self.eps= 0.01       # default learning rate
        self.epsBottom= 0.15 # special learning rate for bottom layer

    def generate(self):
        """
        Generate a pattern d.
        """
        x= bernoulliSample(sigmoid( self.bG))
        y= bernoulliSample(sigmoid( np.dot(self.wG, x+[1])))
        d= bernoulliSample(sigmoid( np.dot(self.vG, y+[1])))
        return d
    
    def wake(self, d):
        """
        One wake learning cycle, given pattern d applied at the bottom.
        """
        # Upward (recognition) pass.
        y= bernoulliSample(sigmoid( np.dot(self.vR, d+[1])))
        x= bernoulliSample(sigmoid( np.dot(self.wR, y+[1])))

        # Downward (generation) pass.
        px= sigmoid(self.bG)
        py= sigmoid(np.dot(self.wG, x+[1]))
        pd= sigmoid(np.dot(self.vG, y+[1]))
        
        # Adjust generative weights by delta rule.
        self.bG += self.eps * (x - px)
        self.wG += self.eps * np.outer(y - py, x+[1])
        self.vG += self.epsBottom * np.outer(d - pd, y+[1])

    def sleep(self):
        """
        One sleep learning cycle.
        """
        # Initiate a dream!
        x = bernoulliSample(sigmoid(self.bG))

        # Pass dream signal downward to generate a pattern.
        y = bernoulliSample(sigmoid( np.dot(self.wG, x+[1])))
        d = bernoulliSample(sigmoid( np.dot(self.vG, y+[1])))

        # Pass back up through recognition network, saving computed probabilities.
        py = sigmoid(np.dot(self.vR, d+[1]))
        px = sigmoid(np.dot(self.wR, y+[1]))
        
        # Adjust recognition weights by delta rule.
        self.vR += self.epsBottom * np.outer(y - py, d+[1])
        self.wR += self.eps * np.outer(x - px, y+[1])


   def learn(self, world, nCycles):
        """
        Run for a given number of wake-sleep cycles to learn this world.
        """
        for t in range(nCycles):
            d = list(world.keys()[np.random.choice(len(world), p=world.values())])
            self.wake(d)
            self.sleep()

    def estimateModel(self, nSamples):
        """
        Generate many samples in order to estimate pattern probabilities.
        probG[d] will be the estimated probability that the HM generates pattern d.
        """
        dp= 1.0 / nSamples
        probG= dict()
        for count in range(nSamples):
            d= tuple(self.generate())
            if d in probG:
                probG[d] += dp
            else:
                probG[d] = dp
        return probG
