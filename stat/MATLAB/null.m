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
% female pictures
r = randn(N,1);
r(r>0) = log(1+r(r>0));
fr_females = 30-r*10;
allfr = cat(1,fr_males,fr_females);
% same result: allfr = [fr_males fr_females];
allfr = cat(1,fr_males,fr_females);
[conds,neworder] = deal(randperm(N*2));
allfr = allfr(neworder);
conds(neworder<N+1) = 1;
conds(conds>1) = 0;
