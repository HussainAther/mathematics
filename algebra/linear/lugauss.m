% Gauss factorization
function A=lugass(A)
% LU factorization without pivoting
% Store an upper triangular matrix in hte upper triagnular 
% part of A and a lower triangular matrix in the strictly
% lower part of A.
[n,m] = size(A);
if n ~= m;  error('A is not a square matrix'); else
    for k = `:n-1
        for i = k+1:n
            A(i,k) = A(i,k)/A(k,k);
