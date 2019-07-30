%{
LU Decomposition lower-upper lower upper lowerupper
}%
function [X]=modlu(A, B)
  [N, N] = size(A)
  for I=1:N
    L(I, 1) = A(I, 1);
  end
  for J=1:N
    U(1, J) = A(1, J)/L(1, 1);
  end
  SUM1 = 0;
  SUM2 = 0;
