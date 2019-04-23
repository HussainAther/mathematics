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
