%{
Signal detection theory.
}%
% step 1
hitP = 22/30;
faP = 3/30;
% step 2hitZ = norminv(hitP);
faZ = norminv(faP);
% step 3
dPrime = hitZ-faZ;
dp2plot = 1; % soft-coding
tol = .01;
idx = find(dp>dp2plot-tol & dp<dp2plot+tol);
