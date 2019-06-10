"""
Deep belief network DBN dbn. We create this by stacking several RBMs (Restricted Boltzmann machines
rbm) on top of each other. The hidden layer of the RBM at layer i becomes the input of the
RBM at layer i+1. The first layer RBM gets as input the input of the network, and the 
hidden layer of the last RBM represents the output. When used for classification, 
the DBN is treated as a MLP, by adding a logistic regression layer on top.
"""

class DBN(object):
    """
    Deep Belief Network
    """
    def __init__(self, numpy_rng, theano_rng=None, n_ins=784,
                 hidden_layers_sizes=[500, 500], n_outs=10):
        """
        This class is made to support a variable number of layers.
        numpy_rng is the random state number. numpy_rng is the generator
        to draw initial weights. theano_rng is for tensor's theano rng.
        n_ins is an integer of the input dimension. hidden_layer_sizes is the
        intermediate layers size. n_outs is output dimension.
        """
        self.sigmoid_layers = []
        self.rbm_layers = []
        self.params = []
        self.n_layers = len(hidden_layers_sizes)
        assert self.n_layers > 0
        if not theano_rng:
            theano_rng = MRG_RandomStreams(numpy_rng.randint(2 ** 30))
        # Alllocate symbolic variables for the data
        # the data is presented as rasterized images
        self.x = T.matrix("x")
        # The labels are presented as 1D vector of [int] labels
        self.y = T.ivector("y")
