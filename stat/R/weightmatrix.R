"Weight (weight) matrix."
reconstruction.weights.2 <- function(x, neighbors, alpha) {
    n = nrow(x)
    w = sapply(1:n, local.weights.for.index, x = x, NNs = neighbors, alpha = alpha)
    w = t(w)
    return(w)
}
"Manifold coordinates from approximation weights by finding eigenfunctions."
coords.from.weights <- function(w, q, tol = 1e-07) {
    n = nrow(w)
    stopifnot(ncol(w) == n)
    stopifnot(all(abs(rowSums(w) - 1) < tol))
    M = t(diag(n) - w) %*% (diag(n) - w)
    soln = eigen(M)
    coords = soln$vectors[, ((n - q):(n - 1))]
    return(coords)
}
