function optgen(wd_coefficient, n_hid, n_iters, learning_rate, momentum_multiplier, do_early_stopping, mini_batch_size)
    % Optimization and generalization algorithm
    warning('error', 'Octave:broadcast');
    if exist('page_output_immediately'), page_output_immediately(1); end
    more off;
    model = initial_model(n_hid);
    from_data_file = load('data.mat');
    datas = from_data_file.data;
    n_training_cases = size(datas.training.inputs, 2);
    if n_iters ~= 0, test_gradient(model, datas.training, wd_coefficient); end

    % optimization
    theta = model_to_theta(model);
    momentum_speed = theta * 0;
    training_data_losses = [];
    validation_data_losses = [];
    if do_early_stopping,
        best_so_far.theta = -1; % this will be overwritten soon
        best_so_far.validation_loss = inf;
        best_so_far.after_n_iters = -1;
    end
    for optimization_iteration_i = 1:n_iters,
        model = theta_to_model(theta);
        training_batch_start = mod((optimization_iteration_i-1) * mini_batch_size, n_training_cases)+1;
        training_batch.inputs = datas.training.inputs(:, training_batch_start : training_batch_start + mini_batch_size - 1);
        training_batch.targets = datas.training.targets(:, training_batch_start : training_batch_start + mini_batch_size - 1);
        gradient = model_to_theta(d_loss_by_d_model(model, training_batch, wd_coefficient));
        momentum_speed = momentum_speed * momentum_multiplier - gradient;
        theta = theta + momentum_speed * learning_rate;
        model = theta_to_model(theta);
        training_data_losses = [training_data_losses, loss(model, datas.training, wd_coefficient)];
        validation_data_losses = [validation_data_losses, loss(model, datas.validation, wd_coefficient)];
        if do_early_stopping && validation_data_losses(end) < best_so_far.validation_loss,
            best_so_far.theta = theta; % this will be overwritten soon
            best_so_far.validation_loss = validation_data_losses(end);
            best_so_far.after_n_iters = optimization_iteration_i;
        end
        if mod(optimization_iteration_i, round(n_iters/10)) == 0,
            fprintf('After %d optimization iterations, training data loss is %f, and validation data loss is %f\n', optimization_iteration_i, training_data_losses(end), validation_data_losses(end));
        end
        if n_iters ~= 0, test_gradient(model, datas.training, wd_coefficient); end % check again, this time with more typical parameters
        if do_early_stopping,
            fprintf('Early stopping: validation loss was lowest after %d iterations. We chose the model that we had then.\n', best_so_far.after_n_iters);
            theta = best_so_far.theta;
        end
        % the optimization is finished. Now do some reporting.
        model = theta_to_model(theta);
        if n_iters ~= 0,
            clf;
            hold on;
            plot(training_data_losses, 'b');
            plot(validation_data_losses, 'r');
            legend('training', 'validation');
            ylabel('loss');
            xlabel('iteration number');
            hold off;
        end
        datas2 = {datas.training, datas.validation, datas.test};
        data_names = {'training', 'validation', 'test'};
        for data_i = 1:3,
            data = datas2{data_i};
            data_name = data_names{data_i};
            fprintf('\nThe loss on the %s data is %f\n', data_name, loss(model, data, wd_coefficient));
            if wd_coefficient~=0,
                fprintf('The classification loss (i.e. without weight decay) on the %s data is %f\n', data_name, loss(model, data, 0));
          end
          fprintf('The classification error rate on the %s data is %f\n', data_name, classification_performance(model, data));
        end
end

function test_gradient(model, data, wd_coefficient)
    base_theta = model_to_theta(model);
    h = 1e-2;
    correctness_threshold = 1e-5;
    analytic_gradient = model_to_theta(d_loss_by_d_model(model, data, wd_coefficient));
    % Test the gradient not for every element of theta, because that's a lot of work. Test for only a few elements.
    for i = 1:100,
        test_index = mod(i * 1299721, size(base_theta,1)) + 1; % 1299721 is prime and thus ensures a somewhat random-like selection of indices
        analytic_here = analytic_gradient(test_index);
        theta_step = base_theta * 0;
        theta_step(test_index) = h;
        contribution_distances = [-4:-1, 1:4];
        contribution_weights = [1/280, -4/105, 1/5, -4/5, 4/5, -1/5, 4/105, -1/280];
        temp = 0;
        for contribution_index = 1:8,
            temp = temp + loss(theta_to_model(base_theta + theta_step * contribution_distances(contribution_index)), data, wd_coefficient) * contribution_weights(contribution_index);
        end
        fd_here = temp / h;
        diff = abs(analytic_here - fd_here);
        % fprintf('%d %e %e %e %e\n', test_index, base_theta(test_index), diff, fd_here, analytic_here);
        if diff < correctness_threshold, continue; end
        if diff / (abs(analytic_here) + abs(fd_here)) < correctness_threshold, continue; end
        error(sprintf('Theta element #%d, with value %e, has finite difference gradient %e but analytic gradient %e. That looks like an error.\n', test_index, base_theta(test_index), fd_here, analytic_here));
    end
    fprintf('Gradient test passed. That means that the gradient that your code computed is within 0.001%% of the gradient that the finite difference approximation computed, so the gradient calculation procedure is probably correct (not certainly, but probably).\n');
end

function ret = logistic(input)
    ret = 1 ./ (1 + exp(-input));
end

function ret = logistic_derivative(input)
    ret = logistic(input);
    ret = ret .* (1.-ret);
end

function ret = log_sum_exp_over_rows(a)
    % a is always a column vector
    % This computes log(sum(exp(a), 1)) in a numerically stable way
    maxs_small = max(a, [], 1);     %max element in each column
    num_rows = size(a, 1);          
    maxs_big = repmat(maxs_small, [num_rows, 1]); % stacks matrix num_rows times vertically i.e. adds rows
    ret = log(sum(exp(a - maxs_big), 1)) + maxs_small;
end

function [log_class_prob, class_prob] = softmax(class_input)
    % "Numerically stable" means that this way, there will never be really big numbers involved.
    % Octave isn't well prepared to deal with really large numbers, like the number 10 to the power 1000. Computations with such numbers get unstable, so we avoid them.
    class_normalizer = log_sum_exp_over_rows(class_input); % log(sum(exp of class_input)) is what we subtract to get properly normalized log class probabilities. size: <1> by <number of data cases>
    log_class_prob = class_input - repmat(class_normalizer, [size(class_input, 1), 1]); % log of probability of each class. size: <number of classes, i.e. 10> by <number of data cases>
    class_prob = exp(log_class_prob); % probability of each class. Each column (i.e. each case) sums to 1. size: <number of classes, i.e. 10> by <number of data cases>
end

function ret = loss(model, data, wd_coefficient)
    % model.input_to_hid is a matrix of size <number of hidden units> by <number of inputs i.e. 256>. It contains the weights from the input units to the hidden units.
    % model.hid_to_class is a matrix of size <number of classes i.e. 10> by <number of hidden units>. It contains the weights from the hidden units to the softmax units.
    % data.inputs is a matrix of size <number of inputs i.e. 256> by <number of data cases>. Each column describes a different data case. 
    % data.targets is a matrix of size <number of classes i.e. 10> by <number of data cases>. Each column describes a different data case. It contains a one-of-N encoding of the class, i.e. one element in every column is 1 and the others are 0.
     
    % Before we can calculate the loss, we need to calculate a variety of intermediate values, like the state of the hidden units.
    hid_input = model.input_to_hid * data.inputs; % input to the hidden units, i.e. before the logistic. size: <number of hidden units> by <number of data cases>
    hid_output = logistic(hid_input); % output of the hidden units, i.e. after the logistic. size: <number of hidden units> by <number of data cases>
    class_input = model.hid_to_class * hid_output; % input to the components of the softmax. size: <number of classes, i.e. 10> by <number of data cases>  
    
    %softmax
    [log_class_prob, class_prob] = softmax(class_input); 
    
    classification_loss = -mean(sum(log_class_prob .* data.targets, 1)); % select the right log class probability using that sum; then take the mean over all data cases.
    wd_loss = sum(model_to_theta(model).^2)/2*wd_coefficient; % weight decay loss. very straightforward: E = 1/2 * wd_coeffecient * theta^2
    ret = classification_loss + wd_loss;
end
