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
  for J = 2:N
    for I = J:N
      SUM1 = 0;
      for K = 1:J-1
        SUM1 = SUM1 + [L(I, K) * U(K, J)];
        end
        L(I, J) = [A(I, J) - SUM1];
    end
    U(J, J) = 1;
    for I = J+1:N;
