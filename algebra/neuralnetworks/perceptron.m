function w=perce(X, y, w_ini)
  [1, N] = size(X);
  max_iter = 10000; % maximum number of iterations
  w = w_ini; % initialization of the parameter vector
  iter = 0; % iteratiaon counter
  mis_clas = N; % number of misclassified vectors
  while (mis_clas > 0) && (iter < max_iter)
    iter = iter + 1;

   
