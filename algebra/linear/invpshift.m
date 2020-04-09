function [lambda ,x,iter ] = invshift (A,mu ,tol ,nmax ,x0)
% INVSHIFT Inverse power method with shift
% LAMBDA=INVSHIFT (A) computes the eigenvalue of A of
% minimum modulus with the inverse power method.
% LAMBDA=INVSHIFT (A,MU) computes the eigenvalue of A
% closest to the given number (real or complex) MU.
% LAMBDA=INVSHIFT (A,MU ,TOL ,NMAX ,X0) uses an absolute
% error tolerance TOL (the default is 1.e -6) and a
% maximum number of iterations NMAX (the default is
% 100), starting from the initial vector X0.
% [LAMBDA ,V,ITER ]= INVSHIFT (A,MU ,TOL ,NMAX ,X0) also
% returns the eigenvector V such that A*V=LAMBDA*V and
% the iteration number at which V was computed.
[n,m] = size (A);
if n ~= m, error('Only for square matrices '); end
if nargin == 1
    x0 = rand(n ,1); nmax = 100; tol = 1.e -06; mu = 0;
elseif nargin == 2
    x0 = rand(n ,1); nmax = 100; tol = 1.e -06;
end
