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
[a,b,c,d,e] = deal(rand)
mean(fr_males)
mean(allfr(conds==1))
fakeconds = randperm(N*2);
fakeconds(fakeconds<N+1) = 1;
fakeconds(fakeconds>1) = 0;
mean(allfr(conds==1)) - mean(allfr(conds==0)) 
mean(allfr(fakeconds==1)) - mean(allfr(fakeconds==0))

nPerms = 1000;
permdiffs = zeros(nPerms,1);
for permi=1:nPerms
    fconds = randperm(N*2);
    fconds(fconds<N+1) = 1;
    fconds(fconds>1) = 0;
    permdiffs(permi) = ...
mean(allfr(fconds==0))-mean(allfr(fconds==1));
end

hist(permdiffs,50)
hold on 
obsval=mean(allfr(conds==0))-mean(allfr(conds==1)); 
plot([obsval obsval],get(gca,'ylim'))
z = (obsval-mean(permdiffs)) / std(permdiffs);
p = 1-normcdf(abs(z));
