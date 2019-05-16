"Gaussian processes in Stan (stan). Use Gaussian process prior and analytic
and non-analytic Gaussian process posteriors."
library(rstan)
rstan_options(auto_write = TRUE)
options(mc.cores = parallel::detectCores())
source("gp_utility.R")
