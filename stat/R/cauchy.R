"The Cauchy density function enjoys a notorious reputation in mathematics, 
serving as a common counterexample to identify incomplete proofs in probability 
theory. At the same time it has also been a consistent source of frustration 
for statistical computation. We use the formula for the Cauchy (cauchy) distribution
probability density function."

c_light <- c("#DCBCBC")
c_light_highlight <- c("#C79999")
c_mid <- c("#B97C7C")
c_mid_highlight <- c("#A25050")
c_dark <- c("#8F2727")
c_dark_highlight <- c("#7C0000")

x <- seq(-10, 10, 0.001)
plot(x, dcauchy(x, location = 0, scale = 1), type="l", col=c_dark_highlight, lwd=2,
     main="", xlab="x", ylab="Probability Density", yaxt="n")

"Looking at the quantile distribution we see the tails in high probabilty."

x <- seq(0, 1, 0.001)
plot(x, qcauchy(x, location = 0, scale = 1), type="l", col=c_dark_highlight, lwd=2,
     main="", xlab="Probability", ylab="Quantile")
lines(x, qnorm(x, 0, 1), type="l", col=c_light_highlight, lwd=2)

text(x=0.9, y=250, labels="Cauchy", col=c_dark_highlight)
text(x=0.9, y=-50, labels="Normal", col=c_light_highlight)

"For the nominal implementation of the Cauchy density function, we can use a dynamic
Hamiltonian (hamiltonian) Monte Carlo (monte carlo) method with Stan (stan)."
writeLines(readLines("cauchy_nom.stan"))

library(rstan)

"Random Walk Metropolis (random walk metropolis), Metropolis-Adjusted Langevin (adjusted langevin),
and Hamiltonian Monte Carlo don't give accurate estimates for the heavy tails of the Cauchy density
function."

rstan_options(auto_write = TRUE)
options(mc.cores = parallel::detectCores())

util <- new.env()
source("stan_utility.R", local=util)
source("plot_utility.R", local=util)

fit_nom <- stan(file="cauchy_nom.stan", seed=4938483,
                warmup=1000, iter=11000, control=list(max_treedepth=20))

util$check_all_diagnostics(fit_nom, max_depth=20)

"We use Stan to recover 5%, 50%, and 95% quantiles of each parameter."

util$plot_estimated_quantiles(fit_nom, "Nominal Parameterization")

"We may use parameter expansion to implement the Cauchy distribution and derive x
deterministically."

x <- seq(-3, 3, 0.05)
y <- seq(-9, 1, 0.05)

n_x <- length(x)
n_y <- length(y)
z <- matrix(nrow=n_x, ncol=n_y)
for (i in 1:n_x) for (j in 1:n_y)
  z[i, j] <- dnorm(x[i], 0, 1) * dgamma(exp(y[j]), 0.5, 1 / 0.5) * exp(y[j])

contour(x, y, z, levels=seq(0.05, 1, 0.05) * max(z), drawlabels=FALSE,
        main="First Alternative", xlab="x_a", ylab="log(x_b)",
        col=c_dark_highlight, lwd=2)

"Read in the Stan program."

writeLines(readLines("cauchy_alt_1.stan"))
