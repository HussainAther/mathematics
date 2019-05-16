"Poisson (poisson) probability mass function that allocates probabilities
across the natural numbers"
c_light <- c("#DCBCBC")
c_light_highlight <- c("#C79999")
c_mid <- c("#B97C7C")
c_mid_highlight <- c("#A25050")
c_dark <- c("#8F2727")
c_dark_highlight <- c("#7C0000")
plot_poisson <- function(l) {
  p <- hist(0, breaks=0:21-0.5, plot=FALSE)
  p$counts <- dpois(0:20, l)

  par(mar = c(8, 6, 0, 0.5))
  plot(p, main="", col="white", border=c_dark_highlight,
       xlab="x", xlim=c(-0.5, 20.5), 
       ylab="Probability Mass", ylim=c(0, 0.2), yaxt="n",
       cex.lab=1.5, cex.axis=1.5, cex.main=1.5, cex.sub=1.5)
}

l <- 5
plot_poisson(l)
"Cumulative distribution function."
B <- 21
xs <- rep(0:B, each=2)
cdfs <- sapply(1:length(xs), function(n) ifelse(n > 1, ppois(xs[n - 1], l), 0))
par(mar = c(8, 6, 0, 0.5))
plot(xs, cdfs, type="l", main="", col=c_dark_highlight, 
     xlab="x", xlim=c(-0.5, 20.5), 
     ylab="Cumulative Probability", ylim=c(0, 1), yaxt="n",
     cex.lab=1.5, cex.axis=1.5, cex.main=1.5, cex.sub=1.5)
"Compute probabilities."
plot_poisson_probs <- function(A, l) {
  bin_edges <- c(A, A[length(A)] + 1) - 0.5
  p_sum <- hist(A[1], breaks=bin_edges, plot=FALSE)
  p_sum$counts <- dpois(A, 5)

  plot(p_sum, col=c_dark, border=c_dark_highlight, add=T)
}

plot_poisson(l)
plot_poisson_probs(A1, l)
sum(sapply(A1, function(x) dpois(x, l)))
"Generate samples from distribution using Poisson probability mass function."
set.seed(8675309)
r_samples <- rpois(1000, l)
writeLines(readLines("generate_poisson.stan"))
simu_data <- list("l" = l)
library(rstan)
rstan_options(auto_write = TRUE)
fit <- stan(file="generate_poisson.stan", data=simu_data, 
            seed=194838, algorithm="Fixed_param",
            iter=1000, warmup=0, chains=1)

stan_samples <- extract(fit)$x[]
plot_poisson(l)
hist(r_samples, breaks=0:21-0.5, 
     col=c_dark_trans, border=c_mid_highlight_trans, probability=T, add=T)
hist(stan_samples, breaks=0:21-0.5, 
     col=c_mid_trans, border=c_light_highlight_trans, probability=T, add=T)
"Empirical cumulative distribution function."
B <- 21
xs <- rep(0:B, each=2)

cdfs <- sapply(1:length(xs), function(n) ifelse(n > 1, ppois(xs[n - 1], l), 0))

par(mar = c(8, 6, 0, 0.5))
plot(xs, cdfs, type="l", main="", col=c_dark_highlight, 
     xlab="x", xlim=c(-0.5, 20.5), 
     ylab="Cumulative Probability", ylim=c(0, 1), yaxt='n',
     cex.lab=1.5, cex.axis=1.5, cex.main=1.5, cex.sub=1.5)

ecdfs <- sapply(1:length(xs), function(n) 
                ifelse(n > 1, length(r_samples[r_samples <= xs[n - 1]]), 0)) / length(r_samples)
lines(xs, ecdfs, col=c_mid_highlight, lwd=2)

ecdfs <- sapply(1:length(xs), function(n) 
                ifelse(n > 1, length(stan_samples[stan_samples <= xs[n - 1]]), 0)) / length(stan_samples)
lines(xs, ecdfs, col=c_light_highlight, lwd=2)

"Facilitate Monte Carlo estimator computation using Welford accumulator to compute empirical
means and variances of a sample."
welford_summary <- function(x) {
  summary = c(0, 0)
  for (n in 1:length(x)) {
    delta <- x[n] - summary[1]
    summary[1] <- summary[1] + delta / (n + 1)
    summary[2] <- summary[2] + delta * (x[n] - summary[1])
  }
  summary[2] <- summary[2] / (length(x) - 1)
  return(summary)
}
compute_mc_stats <- function(x) {
  summary <- welford_summary(x)
  return(c(summary[1], sqrt(summary[2] / length(x))))
}
indicator <- function(x, A) {
  return(ifelse(A[1] <= x & x <= A[length(A)], 1, 0))
}
pushforward_samples = sapply(stan_samples, function(x) indicator(x, A1))
compute_mc_stats(pushforward_samples)
