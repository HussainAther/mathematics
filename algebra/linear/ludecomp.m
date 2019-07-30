%{
LU Decomposition lower-upper lower upper lowerupper
}%
function [X]=modlu(A, B)
  [N, N] = size(A)
  for I=1:N
    L(I, 1) = A(I, 1)
