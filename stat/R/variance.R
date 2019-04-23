"Variance and covariance."
sim.var <- function(n,theta,sigma2,s=1) {
   vars <- apply(rma(n,theta,sigma2,s),2,var)
   return(mean(vars))
}
sim.cov <- function(n,theta,sigma2,s=1) {
  x <- rma(n,theta,sigma2,s)
  covs <- colMeans(x[-1,]*x[-n,])
  return(mean(covs))
}
