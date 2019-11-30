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
# start Gibbs sampler loop
for(t in 2:T){  # full conditional for mu
  m1 <- (h*m + n*tau[t-1]*mean(x))/(h+n*tau[t-1])
  V1 <- 1/(h+n*tau[t-1])
  mu[t] <- rnorm(1,m1,sqrt(V1))
  # full conditional for tau
alph1 <- alph + (n/2); beta1 <- (sum((x-mu[t])̂2)/2) + beta tau[t] <- rgamma(1,alph1,beta1)
sigma2[t] <- 1/tau[t]}
