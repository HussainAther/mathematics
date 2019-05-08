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
