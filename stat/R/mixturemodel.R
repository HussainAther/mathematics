snoqualmie <- scan("http://www.stat.washington.edu/peter/book.data/set1",skip=1)
snoq <- snoqualmie[snoqualmie > 0]
summary(snoq)
library(mixtools)
snoq.k2 <- normalmixEM(snoq, k=2, maxit=100, epsilon=0.01)
plot(hist(snoq, breaks=101), col="grey", border="grey", freq=FALSE,
    xlab="Precipitation (1/100 inch)", main="Precipitation in Snoqualmie Falls")
lines(density(snoq), lty="dashed")
plot.gaussian.clusters <- function(mixture, cluster.number,...) {
    curve(mixture$lambda[cluster.number] *
        dnorm(x, mean=mixture$mu[cluster.number],
        sd = mixture$sigma[cluster.number]), add=TRUE, ...)}
plot(hist(snoq, breaks=101), col="grey", border="grey", freq=FALSE,
    xlab="Precipitation (1/100 inch)", main="Precipitation in Snoqualmie Falls")
    lines(density(snoq), lty=2)
    invisible(sapply(1:2, plot.gaussian.clusters, mixture=snoq.k2))
pnormmix <- function(x,mixture) {
  lambda <- mixture$lambda
  k <- length(lambda)
  pnorm.from.mix <- function(x, cluster) {
    lambda[cluster]*pnorm(x, mean=mixture$mu[cluster],
                            sd=mixture$sigma[cluster])
  }
  pnorms <- sapply(1:k, pnorm.from.mix, x=x)
  return(rowSums(pnorms))
}
