% Least mean squares (lms) algorithm
function w = LMSalg(X, y, w_ini)
  [1, n] = size(X);
  rho = .1; % learning rate
  w = w_ini;
  for i = 1:N
    w = w+(rho/i)*(y(i)-X(:,i)'*w)*X(:,i);
  end
