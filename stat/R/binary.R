"Simulate binary responses from a logistic regression model. Plot a 2D 
logistic regression's probability contours and simulated binary values."
 sim.logistic <- function(x, beta.0, beta, bind = FALSE) {
    require(faraway)
    linear.parts <- beta.0 + (x %*% beta)
    y <- rbinom(nrow(x), size = 1, prob = ilogit(linear.parts))
    if (bind) {
        return(cbind(x, y))
    }
    else {
        return(y)
} }
plot.logistic.sim <- function(x, beta.0, beta, n.grid = 50, labcex = 0.3, col = "grey",
    ...) {
    grid.seq <- seq(from = -1, to = 1, length.out = n.grid)
    plot.grid <- as.matrix(expand.grid(grid.seq, grid.seq))
    require(faraway)
    p <- matrix(ilogit(beta.0 + (plot.grid %*% beta)), nrow = n.grid)
    contour(x = grid.seq, y = grid.seq, z = p, xlab = expression(x[1]), ylab = expression(x[2]),
        main = "", labcex = labcex, col = col)
    y <- sim.logistic(x, beta.0, beta, bind = FALSE)
    points(x[, 1], x[, 2], pch = ifelse(y == 1, "+", "-"), col = ifelse(y ==
        1, "blue", "red"))
    invisible(y)
}
"Binary search function for value x in array v."
binary_search=function(v,x){
  if (x>v[length(v)]){return(NULL)}
  start = 1
  end = length(v)
  while (start<end){
    mid = (start+end) %/% 2 # %/% is the floor division operator
    if (v[mid]>=x){
      end = mid
    }else{
      start = mid+1
    }
  }
  return(start)
}
