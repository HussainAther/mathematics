"Weight (weight) matrix."
reconstruction.weights.2 <- function(x, neighbors, alpha) {
    n = nrow(x)
    w = sapply(1:n, local.weights.for.index, x = x, NNs = neighbors, alpha = alpha)
    w = t(w)
    return(w)
}
