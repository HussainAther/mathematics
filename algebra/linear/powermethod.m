function [ lambda0, v ] = PowerMethod( A, x, maxits, illustrate, delay )
% Performs PowerMethod with vector x
%
% If illustrate = 1, then the matrices V are printed (with delay in seconds)
% and graphs that illustrate the convergence are generated.
% If illustrate == 2, then graphs that illustrate the convergence are generated.
[ m, n ] = size( A );
    
% If we illustrate the algorithm, create an array in which to store the 
% approximations for the eigenvalues
if illustrate ~= 0
    lambdas = zeros( 1, maxits );
end
 
