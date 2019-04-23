"Linear regression for homoskedastic Gaussian noise with one input variable x and a response vairable y."
sim.lm <- function(linfit, test.x) {
    n <- length(test.x)
    sim.frame <- data.frame(x = test.x)
    sigma <- summary(linfit)$sigma * (n - 2)/n
    y.sim <- predict(linfit, newdata = sim.frame)
    y.sim <- y.sim + rnorm(n, 0, sigma)
    sim.frame <- data.frame(sim.frame, y = y.sim)
    return(sim.frame)
}
"Differences in MSE (mean squared error) test statistic."
calc.T <- function(data) {
    MSE.p <- mean((lm(y ~ x, data = data)$residuals)^2)
    MSE.np.bw <- npregbw(y ~ x, data = data)
    MSE.np <- npreg(MSE.np.bw)$MSE
    return(MSE.p - MSE.np)
}
