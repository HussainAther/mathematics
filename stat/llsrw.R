"Iterate to find linear least squares reconstruction weights (least-squares)."
reconstruction.weights <- function(x, neighbors, alpha) {
    stopifnot(is.matrix(x), is.matrix(neighbors), alpha > 0)
    n = nrow(x)
    stopifnot(nrow(neighbors) == n)
    w = matrix(0, nrow = n, ncol = n)
    for (i in 1:n) {
        i.neighbors = neighbors[i, ]
        w[i, i.neighbors] = local.weights(x[i, ], x[i.neighbors, ], alpha)
    }
return(w) }
