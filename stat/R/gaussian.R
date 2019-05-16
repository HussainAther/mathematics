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
"Fit."
simu_fit <- stan(file='simu_gauss.stan', data=simu_data, iter=1,
            chains=1, seed=494838, algorithm="Fixed_param")
f_total <- extract(simu_fit)$f[1,]
y_total <- extract(simu_fit)$y[1,]

true_realization <- data.frame(f_total, x_total)
names(true_realization) <- c("f_total", "x_total")

observed_idx <- c(50*(0:10)+1)
N = length(observed_idx)
x <- x_total[observed_idx]
y <- y_total[observed_idx]

plot(x_total, f_total, type="l", lwd=2, xlab="x", ylab="y",
     xlim=c(-10, 10), ylim=c(-10, 10))
points(x_total, y_total, col="white", pch=16, cex=0.6)
points(x_total, y_total, col=c_mid_teal, pch=16, cex=0.4)
points(x, y, col="white", pch=16, cex=1.2)
points(x, y, col="black", pch=16, cex=0.8)
"Predict."
N_predict <- N_total
x_predict <- x_total
y_predict <- y_total
stan_rdump(c("N", "x", "y",
             "N_predict", "x_predict", "y_predict",
             "sample_idx"), file="gp.data.R")
data <- read_rdump("gp.data.R")
stan_rdump(c("f_total", "x_total", "sigma_true"), file="gp.truth.R")
"Construct the prior data generating process conditioned on the true realization of the 
Gaussian process."
f_data <- list(sigma=sigma_true, N=N_total, f=f_total)
dgp_fit <- stan(file='simu_gauss_dgp.stan', data=f_data, iter=1000, warmup=0,
                chains=1, seed=5838298, refresh=1000, algorithm="Fixed_param")
