"Turn a time series into a design matrix for regression."
design.matrix.from.ts <- function(ts, order, right.older = TRUE) {
    n <- length(ts)
    x <- ts[(order + 1):n]
    for (lag in 1:order) {
        if (right.older) {
            x <- cbind(x, ts[(order + 1 - lag):(n - lag)])
        }
        else {
            x <- cbind(ts[(order + 1 - lag):(n - lag)], x)
} }
    lag.names <- c("lag0", paste("lag", 1:order, sep = ""))
    if (right.older) {
        colnames(x) <- lag.names
    }
    else {
        colnames(x) <- rev(lag.names)
}
    return(as.data.frame(x))
}
