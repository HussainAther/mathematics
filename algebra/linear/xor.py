import numpy as np

"""
XOR Gate using backpropagation
"""

inputLayerNeurons, hiddenLayerNeurons, outputLayerNeurons = 2,2,1
hidden_weights = np.random.uniform(size=(inputLayerNeurons,hiddenLayerNeurons))
hidden_bias =np.random.uniform(size=(1,hiddenLayerNeurons))
output_weights = np.random.uniform(size=(hiddenLayerNeurons,outputLayerNeurons))
output_bias = np.random.uniform(size=(1,outputLayerNeurons))
