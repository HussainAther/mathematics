"Generate heteroskedastic data and fit ordinary least squares (OLS ols) regression."
ols.heterosked.example = function(n) {
    y = 3 - 2 * x + rnorm(n, 0, sapply(x, function(x) {
        1 + 0.5 * x^2
    }))
    fit.ols = lm(y ~ x)
    return(fit.ols$coefficients - c(3, -2))
}
ols.heterosked.error.stats = function(n, m = 10000) {
    ols.errors.raw = t(replicate(m, ols.heterosked.example(n)))
    intercept.se = sd(ols.errors.raw[, "(Intercept)"])
    slope.se = sd(ols.errors.raw[, "x"])
    return(c(intercept.se = intercept.se, slope.se = slope.se))
}
"Linear (linear) regression of heteroskedastic data using weight least-squared (wls)
regression."
wls.heterosked.example = function(n) {
    y = 3 - 2 * x + rnorm(n, 0, sapply(x, function(x) {
        1 + 0.5 * x^2
    }))
    fit.wls = lm(y ~ x, weights = 1/(1 + 0.5 * x^2))
    return(fit.wls$coefficients - c(3, -2))
}
wls.heterosked.error.stats = function(n, m = 10000) {
    wls.errors.raw = t(replicate(m, wls.heterosked.example(n)))
    intercept.se = sd(wls.errors.raw[, "(Intercept)"])
    slope.se = sd(wls.errors.raw[, "x"])
    return(c(intercept.se = intercept.se, slope.se = slope.se))
}
"Iterate the regression function and estimate variance function.
Use unweighted linear regression then alternate between wls for 
getting the regression and kernel smoothing it for the variance."
iterative.wls <- function(x, y, tol = 0.01, max.iter = 100) {
    iteration <- 1
    old.coefs <- NA
    regression <- lm(y ~ x)
    coefs <- coefficients(regression)
    while (is.na(old.coefs) || ((max(coefs - old.coefs) > tol) && (iteration <
        max.iter))) {
        variance <- npreg(residuals(regression)^2 ~ x)
        old.coefs <- coefs
        iteration <- iteration + 1
        regression <- lm(y ~ x, weights = 1/fitted(variance))
        coefs <- coefficients(regression)
}
    return(list(regression = regression, variance = variance, iterations = iteration))
}
"Squared residuals from a linear model plotted against duration along with the unconditional,
homoskedastic variance implicit in OLS (ols) and a kernel-regression estimate of the conditional
variance."
library(MASS)
data(geyser)
geyser.ols <- lm(waiting ~ duration, data = geyser)
plot(geyser$duration, residuals(geyser.ols)^2, cex = 0.5, pch = 16, xlab = "Duration (minutes)",
ylab = expression(`Squared residuals of linear model `(minutes^2))) geyser.var <- npreg(residuals(geyser.ols)^2 ~ geyser$duration) duration.order <- order(geyser$duration) lines(geyser$duration[duration.order], fitted(geyser.var)[duration.order]) abline(h = summary(geyser.ols)$sigma^2, lty = "dashed")
legend("topleft", legend = c("data", "kernel variance", "homoskedastic (OLS)"),
    lty = c("blank", "solid", "dashed"), pch = c(16, NA, NA))
