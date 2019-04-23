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
