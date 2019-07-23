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
hdLayerResp = inputs(ini,:) * weights_i2h; 
hdLayerResp = 2./(1+exp(-hdLayerResp'*2))-1;
otLayerResp = hdLayerResp' * weights_h2o; 
otLayerResp = 2./(1+exp(-otLayerResp'*2))-1;

