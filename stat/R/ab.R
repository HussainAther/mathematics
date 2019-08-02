"Bayesian A/B testing."
# Number of random draws from the prior
n_draws <- 10000

prior <- ... # Here you sample n_draws draws from the prior  
hist(prior) # It's always good to eyeball the prior to make sure it looks ok.

generative_model <- function(parameters) {
  ...
}

sim_data <- rep(NA, n_draws)
for(i in 1:n_draws) {
  sim_data[i] <- generative_model(prior[i])
}

posterior <- prior[sim_data == observed_data] 

hist(posterior) # Eyeball the posterior
length(posterior) # See that we got enought draws left after the filtering.
                  # There are no rules here, but you probably want to aim
                  # for >1000 draws.

median(posterior)
quantile(posterior, c(0.025, 0.975))
