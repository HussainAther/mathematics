# Uniformly most powerful test for normal distribution (ump)
# The "UMPNormal" function returns the critical points required for the UMP test for a sample from normal distribution. The standard deviation is assumed to be known. 
UMPNormal <-
function(mu0, sigma, n,alpha)  {
  mu0-qnorm(alpha)*sigma/sqrt(n)
}
