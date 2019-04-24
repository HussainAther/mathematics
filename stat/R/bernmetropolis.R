"Apply the Metropolis (Metropolis-Hastings metropolis hastings) algorithm to estimate
a binomial proportion."
# Specify the data, to be used in the likelihood function.
# This is a vector with one component per flip,
# in which 1 means a "head" and 0 means a "tail".
myData=c(1,1,1,1,1,1,1,1,1,1,1,0,0,0)

# Define the Bernoulli likelihood function, p(D|theta).
# The argument theta could be a vector, not just a scalar.
likelihood = function( theta , data ) {
    z=sum(data==1)
    N = length(data)
    pDataGivenTheta = theta^z * (1-theta)^(N-z)
