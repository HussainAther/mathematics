# Uniformly most powerful test for an exponential distribution
# A function is defined here which will return the uniformly most powerful test for exponential distribution. The function needs a simple use of the "qgamma" function. 
UMPExponential <-
function(theta0, n, alpha){
  t <- qgamma(1-alpha, shape=n,scale=theta0)
  return(t)
}
