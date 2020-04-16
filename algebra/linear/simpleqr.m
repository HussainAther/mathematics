function [ Ak, V ] = SimpleQRAlg( A, maxits, illustrate, delay )
% Performs a simple QR algorithm (with full matrix).
%
% If illustrate = 1, then the matrices are printed (with delay in seconds)
% and graphs that illustrate the convergence are generated.
[ m, n ] = size( A );
    
% Initialize the matrix in which the eigenvectors are accumulated.
% V = I
V = eye( m, m );
    
% Ak holds iteration A^{(k)}
Ak = A;
