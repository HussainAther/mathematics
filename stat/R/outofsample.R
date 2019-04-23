"Out-of-sample error (oos OOS out of sample error) for the nearly-linear problem
as a function of n. Evaluate generalization error by averaging over many samples."
nearly.linear.out.of.sample = function(n) {
    x <- seq(from = 0, to = 3, length.out = n)
    y <- h(x) + rnorm(n, 0, 0.15)
    data <- data.frame(x = x, y = y)
    y.new <- h(x) + rnorm(n, 0, 0.15)
    sim.lm <- lm(y ~ x, data = data)
    lm.mse <- mean((fitted(sim.lm) - y.new)^2)
    sim.np.bw <- npregbw(y ~ x, data = data)
    sim.np <- npreg(sim.np.bw)
    np.mse <- mean((fitted(sim.np) - y.new)^2)
    mses <- c(lm.mse, np.mse)
    return(mses)
}
nearly.linear.generalization <- function(n, m = 100) {
    raw <- replicate(m, nearly.linear.out.of.sample(n))
    reduced <- rowMeans(raw)
    return(reduced)
}
