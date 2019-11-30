# Uniformly most powerful test
# A simple and straightforward function for obtaining the UMP test for a random sample from uniform distribution. 
UMPUniform <-
function(theta0,n,alpha)  return(theta0*(1-alpha)^{1/n})
