"When smoothing one dimensional data, we want to find an approximation to the true conditional
expectation or reegression function μ. We were controlling how smooth we make indirectly through
the bandwith of the kernels, but we can use a more direct method of controlling smoothness itself by
minimizing the spline objective function."
require(pdfetch)
sp <- pdfetch_YAHOO("SPY", fields = "adjclose", from = as.Date("1993-02-09"),
    to = as.Date("2015-02-09"))
sp <- diff(log(sp))
sp <- sp[-1]
sp.today <- head(sp, -1)
sp.tomorrow <- tail(sp, -1)
coefficients(lm(sp.tomorrow ~ sp.today))
predict(sp.spline, x = 0.01)
"Plot the log-returns data and some less smooth splines in red (lambda = 2.88x-4 and 1.06e-8)."
plot(as.vector(sp.today), as.vector(sp.tomorrow), xlab = "Today's log-return", ylab = "Tomorrow's log-return", pch = 16, cex = 0.5, col = "grey")
abline(lm(sp.tomorrow ~ sp.today), col = "darkgrey")
sp.spline <- smooth.spline(x = sp.today, y = sp.tomorrow, cv = TRUE)
lines(sp.spline)
lines(smooth.spline(sp.today, sp.tomorrow, spar = 1.5), col = "blue")
lines(smooth.spline(sp.today, sp.tomorrow, spar = 2), col = "blue", lty = 2)
lines(smooth.spline(sp.today, sp.tomorrow, spar = 1.1), col = "red")
lines(smooth.spline(sp.today, sp.tomorrow, spar = 0.5), col = "red", lty = 2)
"Find confidence bands for the spline."
sp.frame <- data.frame(today = sp.today, tomorrow = sp.tomorrow)
sp.resampler <- function() {
    n <- nrow(sp.frame)
    resample.rows <- sample(1:n, size = n, replace = TRUE)
    return(sp.frame[resample.rows, ])
}
grid.300 <- seq(from = min(sp.today), to = max(sp.today), length.out = 300)
sp.spline.estimator <- function(data, eval.grid = grid.300) {
    fit <- smooth.spline(x = data[, 1], y = data[, 2], cv = TRUE)
    return(predict(fit, x = eval.grid)$y)
}
sp.spline.cis <- function(B, alpha, eval.grid = grid.300) {
    spline.main <- sp.spline.estimator(sp.frame, eval.grid = eval.grid)
    spline.boots <- replicate(B, sp.spline.estimator(sp.resampler(), eval.grid = eval.grid))
    cis.lower <- 2 * spline.main - apply(spline.boots, 1, quantile, probs = 1 -
        alpha/2)
    cis.upper <- 2 * spline.main - apply(spline.boots, 1, quantile, probs = alpha/2)
    return(list(main.curve = spline.main, lower.ci = cis.lower, upper.ci = cis.upper,
        x = eval.grid))
}
sp.cis <- sp.spline.cis(B = 1000, alpha = 0.05)
plot(as.vector(sp.today), as.vector(sp.tomorrow), xlab = "Today's log-return",
ylab = "Tomorrow's log-return", pch = 16, cex = 0.5, col = "grey") abline(lm(sp.tomorrow ~ sp.today), col = "darkgrey")
lines(x = sp.cis$x, y = sp.cis$main.curve, lwd = 2)
lines(x = sp.cis$x, y = sp.cis$lower.ci)
lines(x = sp.cis$x, y = sp.cis$upper.ci)
