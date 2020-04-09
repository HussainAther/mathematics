function [lambda ,x,iter ] = invshift (A,mu ,tol ,nmax ,x0)
% INVSHIFT Inverse power method with shift
% LAMBDA=INVSHIFT (A) computes the eigenvalue of A of
% minimum modulus with the inverse power method.
% LAMBDA=INVSHIFT (A,MU) computes the eigenvalue of A
