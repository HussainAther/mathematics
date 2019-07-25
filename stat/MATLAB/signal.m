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
[yi,xi] = ind2sub(size(dp),idx);
plot(x(xi),x(yi))
respBias = -(hitZ+faZ)/2;
ntrials = 100; nbins = 7;
d = [500+100*randn(ntrials,1) rand(ntrials,1)>.3]; 
d = sortrows(d,1);
