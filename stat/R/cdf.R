"Calculate cumulative distribution using CDF function and confidence bands."
# Two confidence bands for the CDF
cdf.band <- function(n.unif, alpha=.05){
U = runif(n.unif)
x = sort(U) # find the cutoffs
Y = abs(1:n.unif/n.unif - x)
return(quantile(Y, 1-alpha))
}

# Simulate
c = mean(replicate(1000,cdf.band(250)))

# Calculate the bounds
X = rgamma(250,2,2) # 1 draw
## Empirical cdf
x = sort(X)
emp = 1:250/250

## The two bounds
bound.sim = rbind(pmin(emp+c,1), pmax(emp-c,0))
hoef = sqrt(log(2/.05)/(2*250))
bound.hoef = rbind(pmin(emp+hoef,1), pmax(emp-hoef,0))

# Plot
curve(pgamma(x,2,2),from=0,to=5,bty=’n’,xlab=’x’,ylab=’P(X<x)’)
points(x,emp,pch=19,cex=.2)
matlines(x,t(bound.sim),col=2,lty=3)
matlines(x,t(bound.hoef),col=4,lty=3)
