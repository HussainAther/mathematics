function ret = cd1(rbm_w, visible_data)
% <rbm_w> is a matrix of size <number of hidden units> by <number of visible units>
% <visible_data> is a (possibly but not necessarily binary) matrix of size <number of visible units> by <number of data cases>
% The returned value is the gradient approximation produced by CD-1. It's of the same shape as <rbm_w>.
    
    visible_data = sample_bernoulli(visible_data);	%possibly but not necessarily binary
    hidden_sample = sample_bernoulli(visible_state_to_hidden_probabilities(rbm_w, visible_data));
    representation_goodness_gradient = configuration_goodness_gradient(visible_data, hidden_sample);

    reconstruction_visible_sample = sample_bernoulli(hidden_state_to_visible_probabilities(rbm_w, hidden_sample));
	#{	%Question 7 -  sampling the hidden state that results from the "reconstruction" visible state is useless: it does not 
		%change theexpected value of the gradient estimate that CD-1 produces; it only increases its variance. More variance 
		%means that we have to use a smaller learning rate, 

	reconstruction_hidden_sample = sample_bernoulli(visible_state_to_hidden_probabilities(rbm_w, reconstruction_visible_sample));
	reconstruction_goodness_gradient = configuration_goodness_gradient(reconstruction_visible_sample, reconstruction_hidden_sample);
	#}

	%Question 8
	reconstruction_hidden_prob = visible_state_to_hidden_probabilities(rbm_w, reconstruction_visible_sample);
	reconstruction_goodness_gradient = configuration_goodness_gradient(reconstruction_visible_sample, reconstruction_hidden_prob);
	ret = representation_goodness_gradient - reconstruction_goodness_gradient;
	
end
