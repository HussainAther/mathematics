% Gauss factorization
function A=lugass(A)
% LU factorization without pivoting
% Store an upper triangular matrix in hte upper triagnular 
% part of A and a lower triangular matrix in the strictly
% lower part of A.
[n,m] = size(A);

