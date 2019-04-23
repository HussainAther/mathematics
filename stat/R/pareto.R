"Simulator (simulator) and estimator for model-based bootstrapping of the Pareto distribution."
 }
est.pareto <- function(data) {
    pareto.fit(data, threshold = x0)$exponent
}
"Calculate a p-value for the Pareto distribution using the Kolmogorov-Smirnov 
(K-S k-s KS ks) test, and adjust for the way estimating of the scaling exponent moves
the fitted distribution closer to the data."
ks.stat.pareto <- function(x, exponent, x0) {
    x <- x[x >= x0]
    ks <- ks.test(x, ppareto, exponent = exponent, threshold = x0)
    return(ks$statistic)
}
ks.pvalue.pareto <- function(B, x, exponent, x0) {
    testhat <- ks.stat.pareto(x, exponent, x0)
    testboot <- vector(length = B)
    for (i in 1:B) {
        xboot <- rpareto(length(x), exponent = exponent, threshold = x0)
        exp.boot <- pareto.fit(xboot, threshold = x0)$exponent
        testboot[i] <- ks.stat.pareto(xboot, exp.boot, x0)
    }
    p <- (sum(testboot >= testhat) + 1)/(B + 1)
    return(p)
