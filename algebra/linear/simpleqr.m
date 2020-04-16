function [ Ak, V ] = SimpleQRAlg( A, maxits, illustrate, delay )
% Performs a simple QR algorithm (with full matrix)
%
% If illustrate = 1, then the matrices are printed (with delay in seconds)
% and graphs that illustrate the convergence are generated.
