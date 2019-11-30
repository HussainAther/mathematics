"MCMC (Markov chain Monte Carlo) sampling for a normal likelihood
Consider n = 100 observations yi generated in R from a normal density 
with mean 10 and variance 9. The observed mean and variance is likely 
to differ from the simulation values. Consider estimation of the normal 
parameters 𝜇 and 𝜎2 for the likelihood yi ∼ N(𝜇, 𝜎2). Firstly assuming 
an independent normal-gamma prior for 𝜇 and 𝜏 = 1∕𝜎2, one may apply Gibbs 
sampling, namely repetitive sampling from the full conditionals for 𝜇 
and 𝜏 = 1∕𝜎2, set out above. In particular, assume a Ga(1, 1) prior 
and a N(0, 100) prior for 𝜇. Then a code in R for simulating the data, and 
subsequent Gibbs sampling to estimate 𝜇 and 𝜎2, with T = 10000 iterations and B = 1000 for burn-in, is"

# Observations: sample of n=100 from N(10,9)
x <- rnorm(100,10,3); n <- 100; mn.x <- mean(x); var.x <- var(x)
cat("Observed mean ",mn.x, "\n ")
cat("Observed variance ",var.x, "\n ")

# Gibbs Sampling in conjunction with Normal/Gamma Priors
# Parameters for Normal priors on mu, and gamma prior on tau
m<-0;V <-100;h<-1/V;alph <-1;beta <-1
# MCMC sample settings, arrays for holding samples, initial # values (0 for mu, 1 for tau)
  T <- 10000; B <- 1000; TB <- T-B
  mu <-  tau <- sigma2  <- numeric(T);
  mu[1] <- 0; tau[1] <- 1

# Gibbs sampler loop
for(t in 2:T){  # full conditional for mu
  m1 <- (h*m + n*tau[t-1]*mean(x))/(h+n*tau[t-1])
  V1 <- 1/(h+n*tau[t-1])
  mu[t] <- rnorm(1,m1,sqrt(V1))
  # full conditional for tau
alph1 <- alph + (n/2); beta1 <- (sum((x-mu[t])̂2)/2) + beta tau[t] <- rgamma(1,alph1,beta1)
sigma2[t] <- 1/tau[t]}

# Retain samples after Burn-in
mu <- mu[B+1:T]; sigma2 <- sigma2[B+1:T]

# parameter summaries
summary(mu);       quantile(mu[1:TB], c(0.025, 0.05, 0.90, 0.975))
summary(sigma2); quantile(sigma2[1:TB], c(0.025, 0.05, 0.90, 0.975))

# Set up subplots
par(mfrow=c(2,2))

# Trace Plots
plot(mu,type="l");   plot(sigma2,type="l")

# Marginal Posterior Densities
plot(density(mu),col="red",main=expression(paste("Posterior
                                          Density of ",mu)))
plot(density(sigma2),col="blue",main=expression(paste("Posterior
Density of ",sigmâ2)))

# Proposal rejection rates with uniform Metropolis sampling to update mu and sigma
# MCMC sample settings, arrays for holding samples, initial values
T <- 10000; B <- 1000;
mu <- sigma2 <- sig <- numeric(T) ; u.mu <-  u.sig <- runif(T)
sig[1] <- 1; mu[1] <- 0

# totals for rejections of proposals
REJmu <- 0; REJsig <- 0

# log posterior density (up to a constant)
logpost=function(x,mu,sig){logpost= sum(dnorm(x,mu,sig,log=T)) - log(sig)}

# MCMC sampling loop
for (t in 2:T) {mucand <- mu[t-1] + runif(1,-0.5,0.5)
                      sigcand <- abs(sig[t-1] + runif(1,-0.5,0.5))

# accept (or not) proposal for mu
log.alph.mu = logpost(x,mucand,sig[t-1])-logpost(x,mu[t-1],sig[t-1])
if (log(u.mu[t]) < log.alph.mu) mu[t] <- mucand
else { mu[t] <- mu[t-1]; if(t > B) REJmu <- REJmu+1 }

# accept (or not) proposal for sigma
log.alph.sig = logpost(x,mu[t],sigcand)-logpost(x,mu[t],sig[t-1])
if (log(u.sig[t]) < log.alph.sig) sig[t] <- sigcand
else { sig[t] <- sig[t-1]; if (t>B) REJsig <- REJsig+1 }
sigma2[t] <- sig[t]*sig[t]}

# Rejection Rates
cat("Rejection Rate mu = ",REJmu/(T-B), "\n ")
cat("Rejection Rate sigma = ",REJsig/(T-B), "\n ")
