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
        for i in range(self.n_layers):
            # Construct the sigmoidal layer. The size of the input is 
            # either the number of hidden units of the layer below or the 
            # input size if we are on the first layer.
            if i == 0:
                input_size = n_ins
            else:
                input_size = hidden_layers_sizes[i - 1]
            # The input to this layer is either the activation of the
            # hidden layer below or the input of the DBN if you are on
            # the first layer
            if i == 0:
                layer_input = self.x
            else:
                layer_input = self.sigmoid_layers[-1].output
            sigmoid_layer = HiddenLayer(rng=numpy_rng,
                                        input=layer_input,
                                        n_in=input_size,
                                        n_out=hidden_layers_sizes[i],
                                        activation=T.nnet.sigmoid)
            # Add the layer to our list of layers
            self.sigmoid_layers.append(sigmoid_layer)
            self.params.extend(sigmoid_layer.params)
            # Construct an RBM that shared weights with this layer
            rbm_layer = RBM(numpy_rng=numpy_rng,
                            theano_rng=theano_rng,
                            input=layer_input,
                            n_visible=input_size,
                            n_hidden=hidden_layers_sizes[i],
                            W=sigmoid_layer.W,
                            hbias=sigmoid_layer.b)
            self.rbm_layers.append(rbm_layer)
