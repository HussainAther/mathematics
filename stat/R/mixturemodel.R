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
distinct.snoq <- sort(unique(snoq))
tcdfs <- pnormmix(distinct.snoq,mixture=snoq.k2)
ecdfs <- ecdf(snoq)(distinct.snoq)
plot(tcdfs, ecdfs, xlab="Theoretical CDF", ylab="Empirical CDF", xlim=c(0,1),
     ylim=c(0,1))
abline(0,1)
dnormalmix <- function(x,mixture,log=FALSE) {
    lambda <- mixture$lambda
    k <- length(lambda)
    # Calculate share of likelihood for all data for one cluster
    like.cluster <- function(x,cluster) {
    lambda[cluster]*dnorm(x,mean=mixture$mu[cluster],
                            sd=mixture$sigma[cluster])
    }
    # Create array with likelihood shares from all clusters over all data
    likes <- sapply(1:k,like.cluster,x=x)
    # Add up contributions from clusters
    d <- rowSums(likes)
    if (log) {
d <- log(d) }
return(d) }
loglike.normalmix <- function(x,mixture) {
    loglike <- dnormalmix(x,mixture,log=TRUE)
    return(sum(loglike))
}
n <- length(snoq)
data.points <- 1:n
data.points <- sample(data.points) # Permute randomly
train <- data.points[1:floor(n/2)] # First random half is training
test <- data.points[-(1:floor(n/2))] # 2nd random half is testing
candidate.cluster.numbers <- 2:10
loglikes <- vector(length=1+length(candidate.cluster.numbers))
# k=1 needs special handling
mu<-mean(snoq[train]) # MLE of mean
sigma <- sd(snoq[train])*sqrt((n-1)/n) # MLE of standard deviation
loglikes[1] <- sum(dnorm(snoq[test],mu,sigma,log=TRUE))
for (k in candidate.cluster.numbers) {
    mixture <- normalmixEM(snoq[train],k=k,maxit=400,epsilon=1e-2)
    loglikes[k] <- loglike.normalmix(snoq[test],mixture=mixture)
}
plot(x=1:10, y=loglikes,xlab="Number of mixture clusters",
    ylab="Log-likelihood on testing data")
