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
  sum1 = 0;
  sum2 = 0;
  for J = 2:N
    for I = J:N
      sum1 = 0;
      for K = 1:J-1
        sum1 = sum1 + [L(I, K) * U(K, J)];
        end
        L(I, J) = [A(I, J) - sum1];
    end
    U(J, J) = 1;
    for I = J+1:N;
      sum2 = 0;
      for K = 1:J-1
        sum2 = sum2 + [L(J, K) * U(K, I)];
      end
      U(J, I) = [A(J, I) - sum2]/L(J, J);
    end
  end
  L(I, J) = A(I, J) - sum1
  U(J, I) = [A(J, I) - sum2]/L(J, J)
  X = zeros(N, 1);
  C(1) = B(1)/L(1, 1);
  for I = 2:N
    sum3 = 0;
    for K = 1:I-1
      sum3 = sum3 + L(I, K) * C(K);
    end
    C(I) = B(I) - sum3;
  end
  X(N) = C(N)
  for J = N-1:-1:1
    sum4 = 0;
    for K = J+1:N
      sum4 = sum4 + U(J, K) * X(K);
    end
  X(J) = (C(J) - sum4)/L(J,J)
  end
