"Gaussian processes in Stan (stan). Use Gaussian process prior and analytic
and non-analytic Gaussian process posteriors."
library(rstan)
rstan_options(auto_write = TRUE)
options(mc.cores = parallel::detectCores())
source("gp_utility.R")
"Define hyperparameters alpha and rho with measurement variation sigma. Use covariates."
alpha_true <- 3
rho_true <- 5.5
sigma_true <- 2

N_total = 501
x_total <- 20 * (0:(N_total - 1)) / (N_total - 1) - 10

simu_data <- list(alpha=alpha_true, rho=rho_true, sigma=sigma_true,
                  N=N_total, x=x_total)
"Construct marginal covariance matrix. Simulate data using Gaussian variation around
the sampled function. Use nugget or jitter so the marginal covariance matrix before
the Cholesky decomposition stabilizes the numerical calculations."
writeLines(readLines("simu_gauss.stan"))
