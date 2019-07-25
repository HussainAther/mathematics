%{
Null hypothesis testing.
}%
% create Gaussian distribution
r = randn(1000,1);
% skew it
r(r>0) = log(1+r(r>0));
N = 100;
% male pictures
r = randn(N,1);
r(r>0) = log(1+r(r>0));
fr_males = 26-r*10;
