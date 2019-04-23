"Locally (locally) linear embedding."
lle <- function(x, q, k = q + 1, alpha = 0.01) {
    stopifnot(q > 0, q < ncol(x), k > q, alpha > 0)
    kNNs = find.kNNs(x, k)
    w = reconstruction.weights(x, kNNs, alpha)
    coords = coords.from.weights(w, q)
    return(coords)
}
