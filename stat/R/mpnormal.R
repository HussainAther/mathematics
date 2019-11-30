# mpnormal most powerful normal
# The most powerful test for a sample from normal distribution is given here. The test is obtained by an application of the Neyman-Pearson lemma. 
MPNormal <-
function(mu0, mu1, sigma, n,alpha)  {
  if(mu0<mu1) k <- qnorm(alpha,lower.tail = FALSE)*sigma/sqrt(n) + mu0
  if(mu0>mu1) k <- mu0 - qnorm(alpha,lower.tail = FALSE)*sigma/sqrt(n)
  return(k)
}
