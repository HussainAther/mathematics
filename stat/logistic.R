"Synthetic logistic data set."
logistic.map <- function(x, r = 4) {
    r * x * (1 - x)
}
logistic.iteration <- function(n, x.init, r = 4) {
    x <- vector(length = n)
    x[1] <- x.init
    for (i in 1:(n - 1)) {
        x[i + 1] <- logistic.map(x[i], r = r)
    }
return(x) }
x <- logistic.iteration(1000, x.init = runif(1))
y <- x + rnorm(1000, mean = 0, sd = 0.05)
