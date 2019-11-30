# Logistic regression, M-H estimation with and without predictor selection
n = 53;   npar = 5;   T =10000; B=1000; B1 <- B+1

# Input data
y <- c(0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0,0,0,0,0,0,0,1,0,1,1,0,0,0,
0,0,0,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1)
 X <- matrix(c(1,-0.73,0,0,0,
1,-0.58,0,0,0,
.....
1,-0.12,1,1,0,
1,0.23,1,1,1),nrow=53,byrow=T)

# Set up the matrices to calculate posterior mean and sd
    mn <- var <- std <- accrate <- array(0,npar)

# Normal priors on regression coefficients
    mu <- c(0,0.75,0.75,0.75,0.75); sig2 <- c(100,25,25,25,25);
    sig <- sqrt(sig2)

# Parameters for MH updates (Uniform random walk)
    kappa <- c(1,1,1,1,1)

# Initial parameter values
    theta <- c(0,0,0,0,0)

# sampled parameters
    sample <- samp2 <- acc <- array(0, dim=c(T, npar))

# calculate log likelihood
calcLK <- function(n, y, theta, npar, X){ p <- array(0,n); likhood <- 0
    for (i in 1:n) { eta <- sum(theta[1:npar]*X[i,1:npar])
                  p[i] <- 1/(1+exp(-eta))
                  likhood <- likhood + y[i]*log(p[i])+(1-y[i])*log(1-p[i])}
                  likhood}

# log-likelihood for initial parameters
    LK <- calcLK(n, y, theta, npar, X)

# MH updates Start Loop
    for (t in 1:T) { for (i in 1:npar) {

# Candidate using Uniform proposal density
oldtheta <- theta[i]
            theta[i] <- runif(1, theta[i]-kappa[i], theta[i]+kappa[i])

# Likelihood of proposed value
            newLK <- calcLK(n, y, theta, npar, X)
            num <- newLK + log(dnorm(theta[i],mu[i],sig[i]))
            den <- LK + log(dnorm(oldtheta,mu[i],sig[i]))
            A <- min(1,exp(num-den))
            u <- runif(1)

# Accept move with probability A, or stay at existing value
         if (u <= A) {  LK <- newLK; if(t>B) {acc[t,i] <- 1 }}
                else      { theta[i] <- oldtheta ;    if(t>B)
                                          {acc[t,i] <- 0  }}}

# Record parameter values:
for (i in 1:npar) {sample[t,i] <- theta[i]; samp2[t,i] <- theta[i]̂2}}

# posterior means and sd, acceptance rates
for (i in 1:npar) {mn[i] <- sum(sample[B1:T,i])/(T-B)
accrate[i] <- sum(acc[B1:T,i])/(T-B) std[i] <- sqrt((sum(samp2[B1:T,i])-(T-B)*mn[i]̂2)/(T-B-1))}

# examples of numerical/graphical summaries
summary(sample[B1:T,1]);
plot(density(sample[B1:T,1],bw=0.15))
library(LaplacesDemon)

# press enter after message regarding page change
p.interval(sample[B1:T,1], HPD=TRUE, MM=FALSE, plot=TRUE)
