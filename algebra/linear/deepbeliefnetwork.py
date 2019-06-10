import numpy as np

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
        self.logLayer = LogisticRegression(
            input=self.sigmoid_layers[-1].output,
            n_in=hidden_layers_sizes[-1],
            n_out=n_outs)
        self.params.extend(self.logLayer.params)
        # Compute the cost for second phase of training, defined as the
        # negative log likelihood of the logistic regression (output) layer
        self.finetune_cost = self.logLayer.negative_log_likelihood(self.y)
        # Compute the gradients with respect to the model parameters
        # symbolic variable that points to the number of errors made on the
        # minibatch given by self.x and self.y
        self.errors = self.logLayer.errors(self.y)

    def pretraining_functions(self, train_set_x, batch_size, k):
        """
        Generate a list of functions, for performing one step of
        gradient descent at a given layer. The function will require
        as input the minibatch index, and to train an RBM you just
        need to iterate, calling the corresponding function on all
        minibatch indexes. train_x has data for training the RBM.
        batch_size is the size of a batch. k is the number of Gibbs
        steps to do in CD-k.
        """
        # Index to a [mini]batch
        index = T.lscalar('index')  # index to a minibatch
        learning_rate = T.scalar('lr')  # learning rate to use
        # Begining of a batch, given index
        batch_begin = index * batch_size
        # ending of a batch given `index`
        batch_end = batch_begin + batch_size
        pretrain_fns = []
        for rbm in self.rbm_layers:
            # Get the cost and the updates list
            # using CD-k here (persisent=None) for training each RBM.
            # TODO: change cost function to reconstruction error
            cost, updates = rbm.get_cost_updates(learning_rate,
                                                 persistent=None, k=k)
            # Compile the theano function
            fn = theano.function(
                inputs=[index, theano.In(learning_rate, value=0.1)],
                outputs=cost,
                updates=updates,
                givens={
                    self.x: train_set_x[batch_begin:batch_end]
                }
            )
            # Append f to the list of functions
            pretrain_fns.append(fn)
        return pretrain_fns

    def build_finetune_functions(self, datasets, batch_size, learning_rate):
        """
        Generates a function train that implements one step of
        finetuning, a function validate that computes the error on a
        batch from the validation set, and a function test that
        computes the error on a batch from the testing set.
        datasets is a list of pairs of tensors that have all the datasets.
        batch_size is the size of a minibatch, and learning_rate is the learning
        learning rate for finetune stage.        
        """
        (train_set_x, train_set_y) = datasets[0]
        (valid_set_x, valid_set_y) = datasets[1]
        (test_set_x, test_set_y) = datasets[2]
        # Compute number of minibatches for training, validation and testing
        n_valid_batches = valid_set_x.get_value(borrow=True).shape[0]
        n_valid_batches //= batch_size
        n_test_batches = test_set_x.get_value(borrow=True).shape[0]
        n_test_batches //= batch_size
        index = T.lscalar('index')  # index to a [mini]batch
        # Compute the gradients with respect to the model parameters
        gparams = T.grad(self.finetune_cost, self.params)
        # Compute list of fine-tuning updates
        updates = []
        for param, gparam in zip(self.params, gparams):
            updates.append((param, param - gparam * learning_rate))
        train_fn = theano.function(
            inputs=[index],
            outputs=self.finetune_cost,
            updates=updates,
            givens={
                self.x: train_set_x[
                    index * batch_size: (index + 1) * batch_size
                ],
                self.y: train_set_y[
                    index * batch_size: (index + 1) * batch_size
                ]
            }
        )

        test_score_i = theano.function(
            [index],
            self.errors,
            givens={
                self.x: test_set_x[
                    index * batch_size: (index + 1) * batch_size
                ],
                self.y: test_set_y[
                    index * batch_size: (index + 1) * batch_size
                ]
            }
        )
        valid_score_i = theano.function(
            [index],
            self.errors,
            givens={
                self.x: valid_set_x[
                    index * batch_size: (index + 1) * batch_size
                ],
                self.y: valid_set_y[
                    index * batch_size: (index + 1) * batch_size
                ]
            }
        )
        def valid_score():
            """
            Scan the entire validation set from the valid batches.
            """
            return [valid_score_i(i) for i in range(n_valid_batches)]
        def test_score():
            """
            Scan the validation set for test batches.
            """
            return [test_score_i(i) for i in range(n_test_batches)]
        return train_fn, valid_score, test_score

# Set random state
numpy_rng = np.random.RandomState(123)

# Construct the Deep Belief Network
dbn = DBN(numpy_rng=numpy_rng, n_ins=28 * 28,
          hidden_layers_sizes=[1000, 1000, 1000],
          n_outs=10)

