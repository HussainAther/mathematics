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
