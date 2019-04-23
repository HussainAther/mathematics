"Calculate bootstrap standard errors. rboot function generates B bootstrap samples.
simulator is a function that reutrns a surrogate data set in a form suitable for statistic.
bootstrap function takes the output of rboot and applies a summarizing function.
bootstrap.se calls rboot and makes the summarizing function sd that takes a standard
deviation."
rboot <- function(statistic, simulator, B) {
    tboots <- replicate(B, statistic(simulator()))
    if (is.null(dim(tboots))) {
        tboots <- array(tboots, dim = c(1, B))
    }
    return(tboots)
}
bootstrap <- function(tboots, summarizer, ...) {
    summaries <- apply(tboots, 1, summarizer, ...)
    return(t(summaries))
}
bootstrap.se <- function(statistic, simulator, B) {
    bootstrap(rboot(statistic, simulator, B), summarizer = sd)
}
"Bootstrap bias correction function. t.hat is the estimate on the original
data."
bootstrap.bias <- function(simulator, statistic, B, t.hat) {
    expect <- bootstrap(rboot(statistic, simulator, B), summarizer = mean)
    return(expect - t.hat)
}
"Basic bootstrap confidence interval (CI ci)."
equitails <- function(x, alpha) {
    lower <- quantile(x, alpha/2)
    upper <- quantile(x, 1 - alpha/2)
    return(c(lower, upper))
}
bootstrap.ci <- function(statistic = NULL, simulator = NULL, tboots = NULL,
    B = if (!is.null(tboots)) {
        ncol(tboots)
    }, t.hat, level) {
    if (is.null(tboots)) {
        stopifnot(!is.null(statistic))
        stopifnot(!is.null(simulator))
        stopifnot(!is.null(B))
        tboots <- rboot(statistic, simulator, B)
    }
    alpha <- 1 - level
    intervals <- bootstrap(tboots, summarizer = equitails, alpha = alpha)
    upper <- t.hat + (t.hat - intervals[, 1])
    lower <- t.hat + (t.hat - intervals[, 2])
    CIs <- cbind(lower = lower, upper = upper)
    return(CIs)
}
"Bootstrap p-value correction. testhat is the value of hte test statistic
on the actual data. test is a function that takes in a data set and calculates
the test statistic, presuming that large values indicate departure from the null hypothesis."
boot.pvalue <- function(test, simulator, B, testhat) {
    testboot <- rboot(B = B, statistic = test, simulator = simulator)
    p <- (sum(testboot >= testhat) + 1)/(B + 1)
    return(p)
}
"Double (double) bootstrap. The inner or second bootstrap calculates the distribution of nominal
bootstrap p-values. We draw our second-level bootstrap samples from theta.tilde, the bootstrap re-estimate,
not from theta.hat, the data estimate."
doubleboot.pvalue <- function(test, simulator, B1, B2, estimator, thetahat,
    testhat, ...) {
    for (i in 1:B1) {
        xboot <- simulator(theta = thetahat, ...)
        thetaboot <- estimator(xboot)
        testboot[i] <- test(xboot)
        pboot[i] <- boot.pvalue(test, simulator, B2, testhat = testboot[i],
            theta = thetaboot)
    }
    p <- (sum(testboot >= testhat) + 1)/(B1 + 1)
    p.adj <- (sum(pboot <= p) + 1)/(B1 + 1)
    return(p.adj)
}
