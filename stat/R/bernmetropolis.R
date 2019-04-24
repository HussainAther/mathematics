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
    # The theta values passed into this function are generated at random,
    # and therefore might be inadvertently greater than 1 or less than 0.
    # The likelihood for theta > 1 or for theta < 0 is zero: 
    pDataGivenTheta[theta > 1 | theta < 0] = 0
    return(pDataGivenTheta)
}

# Define the prior density function. For purposes of computing p(D),
# at the end of this program, we want this prior to be a proper density. 
# The argument theta could be a vector, not just a scalar.
prior = function(theta) {
    prior = rep(1, length(theta)) # uniform density over [0,1]
    # For kicks, here’s a bimodal prior. To try it, uncomment the next line.
    #prior = dbeta(pmin(2*theta, 2*(1-theta)), 2, 2)
    # The theta values passed into this function are generated at random,
    # and therefore might be inadvertently greater than 1 or less than 0.
    # The prior for theta > 1 or for theta < 0 is zero:
    prior[theta>1|theta<0]=0
    return(prior)
}

# Define the relative probability of the target distribution,
# as a function of vector theta. This target distribution is the 
# unnormalized posterior distribution.
targetRelProb = function(theta, data) {
     targetRelProb = likelihood(theta, data) * prior(theta)
