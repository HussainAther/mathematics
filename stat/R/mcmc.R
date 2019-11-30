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
