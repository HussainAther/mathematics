"Linear regression of heteroskedastic data, using weighted least-squared regression."

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
