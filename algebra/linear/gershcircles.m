function gershcircles(A)
% GERSHCIRCLES plots the Gershgorin circles
% GERSHCIRCLES (A) draws the Gershgorin circles
% the square matrix A and its transpose.
n = size(A);
if n(1) ~= n(2)
    error('Only square matrices ');
else
    n = n(1); circler = zeros(n ,201); circlec = circler;
end
