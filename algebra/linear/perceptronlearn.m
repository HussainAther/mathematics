%% Learns the weights of a perceptron and displays the results.
function [w] = learn_perceptron(neg_examples_nobias,pos_examples_nobias,w_init,w_gen_feas)
%% 
% Learns the weights of a perceptron for a 2-dimensional dataset and plots
% the perceptron at each iteration where an iteration is defined as one
% full pass through the data. If a generously feasible weight vector
% is provided then the visualization will also show the distance
% of the learned weight vectors to the generously feasible weight vector.
% Required Inputs:
%   neg_examples_nobias - The num_neg_examples x 2 matrix for the examples with target 0.
%       num_neg_examples is the number of examples for the negative class.
%   pos_examples_nobias - The num_pos_examples x 2 matrix for the examples with target 1.
%       num_pos_examples is the number of examples for the positive class.
%   w_init - A 3-dimensional initial weight vector. The last element is the bias.
%   w_gen_feas - A generously feasible weight vector.
% Returns:
%   w - The learned weight vector.
%%

num_neg_examples = size(neg_examples_nobias,1);
num_pos_examples = size(pos_examples_nobias,1);
num_err_history = [];
w_dist_history = [];
