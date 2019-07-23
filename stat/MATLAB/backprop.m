%{
Neural network with backpropagation.
}%
inputs = [ 1 0 1; 0 1 1; 1 1 1; 0 0 1 ]; 
output = [ 0; 0; 1; 1 ];
nInputsNodes = size(inputs,2);
nHiddenNodes = 3;
nOutputNodes = 1;
% random initial weights
weights_i2h = randn(nInputsNodes,nHiddenNodes); 
weights_h2o = randn(nHiddenNodes,nOutputNodes); 
l_rate = .2;
