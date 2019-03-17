import numpy as np

"""
The Helmholtz machine was designed to accommodate hierarchical architectures that construct complex
multilayer representations. The model in- volves two interacting networks, one with parameters G
that is driven in the top-down direction to implement the generative model, and the other, with
parameters W , driven bottom-up to implement the recogni- tion model.

The parameters are determined by a modified EM algorithm that results in roughly symmetric updates for the two networks.
"""

def sigmoid(u):
    """
    A vectorized version of the logistic sigmoid firing function.
    """
    return 1/(1 + np.exp(np.negative(u)))

def bernoulliSample( probs ):
    """
    Generate a binary vector according to a vector of probabilities.
    """
    return map( (lambda p : np.random.choice( (1.0,0.0), p=(p,1-p) )), probs )

def intToPattern( i, n ):
    """
    An length n tuple of 0.,1.'s corresponding to the binary form of i.
    """
    return tuple( map(float, bin(i)[2:].zfill(n)))

def patternToString( d, clumpsize ):
    """
    For prettyprinting a real binary pattern list in space-separated clumps.
    """
    s= ""
    for k in range( len(d) ):
        if k%clumpsize == 0:
            s+= " "
        s += "1" if d[k]>0 else "0"
    return s

class HelmholtzMachine:
    def __init__( self, nTop, nMid, nBottom ):
        """
        Construct a 3-layer HM with the given number of neurons at each level.
        """
        # Dimension of pattern vector visible at the bottom.
        self.dimension= nBottom

        # Generative weights (top down)
        self.bG= np.zeros( nTop )
        self.wG= np.zeros( [nMid, nTop+1] )
        self.vG= np.zeros( [nBottom, nMid+1] )
        
        # Recognition weights (bottom up)
        self.vR= np.zeros( [nMid, nBottom+1] )
        self.wR= np.zeros( [nTop, nMid+1] )
        
        # Some default learning rates
        self.eps= 0.01       # default learning rate
        self.epsBottom= 0.15 # special learning rate for bottom layer

    def generate( self ):
        """
        Generate a pattern d.
        """
        x= bernoulliSample( sigmoid( self.bG ) )
        y= bernoulliSample( sigmoid( np.dot(self.wG, x+[1]) ) )
        d= bernoulliSample( sigmoid( np.dot(self.vG, y+[1]) ) )
        return d

