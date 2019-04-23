"K-nearest neighbors (k nearest neighbor knn) of all the row-vectors in a 
data frame. This is slow."
find.kNNs <- function(x, k, ...) {
    x.distances = dist(x, ...)
    x.distances = as.matrix(x.distances)
    kNNs = smallest.by.rows(x.distances, k + 1)
    return(kNNs[, -1])
}
