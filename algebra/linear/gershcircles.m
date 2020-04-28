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
center = diag (A);
radiic = sum(abs(A-diag (center )));
radiir = sum(abs(A’-diag (center )));
one = ones(1 ,201); cosisin = exp(i*[0: pi /100:2* pi]);
figure (1); title('Row circles ');
xlabel('Re'); ylabel('Im');
figure (2); title('Column circles ');
xlabel('Re'); ylabel('Im');
