% Least mean squares (lms) algorithm
function w = LMSalg(X, y, w_ini)
  [1, n] = size(X);
  rho = .1; % learning rate
