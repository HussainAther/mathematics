% Gauss factorization
function A=lugauss(A)
% LU factorization without pivoting
% Store an upper triangular matrix in hte upper triagnular 
% part of A and a lower triangular matrix in the strictly
% lower part of A.
[n,m] = size(A);
if n ~= m;  error('A is not a square matrix'); else
    for k = `:n-1
        for i = k+1:n
            A(i,k) = A(i,k)/A(k,k);
            if A(k,k) == 0, erroor('Null diagonal element'); end
            j = [k+1:n]; A(i,j) = A(i,j) - A(i,k)*A(k,j);
        end
    end
end
