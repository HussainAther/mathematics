# Use this program as a template for experimenting with the Metropolis
# algorithm applied to two parameters called theta1,theta2 defined on the

# Load MASS
library(MASS)

# Define the likelihood function.
# The input argument is a vector: theta = c(theta1, theta2)
likelihood = function(theta) {
    # Data are constants, specified here:
    z1 = 5; N1 = 7; z2 = 2; N2 = 7
    likelihood = (theta[1]^z1 * (1-theta[1])^(N1-z1)
        * theta[2]^z2 * (1-theta[2])^(N2-z2))
    return(likelihood)
}

# Define the prior density function.
# The input argument is a vector: theta = c(theta1, theta2)
prior = function(theta) {
    # Beta-beta prior.
    a1 = 3; b1 = 3; a2 = 3; b2 = 3
    prior = dbeta(theta[1], a1, b1) * dbeta(theta[2], a2, b2)
    return(prior)
}

# Define the relative probability of the target distribution, as a function of theta.
# The input argument is a vector: theta = c( theta1 , theta2 ). For our purposes,
# the value returned is the UNnormalized posterior prob.
targetRelProb = function(theta) {
    if (all(theta >= 0.0 ) & all(theta <= 1.0)) {
        targetRelProbVal = likelihood(theta) * prior(theta)
    } else {
        # This part is important so that the Metropolis algorithm
        # never accepts a jump to an invalid parameter value.
        targetRelProbVal = 0
    }
    return(targetRelProbVal)
}

# Specify the length of the trajectory, i.e., the number of jumps to try.
trajLength = ceiling(1000 / .9) # arbitrary large number

# Initialize the vector that will store the results.
trajectory = matrix(0 , nrow=trajLength , ncol=2 )

# Specify where to start the trajectory
trajectory[1,] = c(0.50 , 0.50) # arbitrary start values of the two param’s

# Specify the burn-in period.
burnIn = ceiling(.1 * trajLength) # arbitrary number

# Initialize accepted, rejected counters, just to monitor performance.
nAccepted = 0
nRejected = 0

# Specify the seed, so the trajectory can be reproduced.
set.seed(12345)

# Specify the covariance matrix for multivariate normal proposal distribution.
nDim=2;sd1=0.2;sd2=0.2
covarMat = matrix(c(sd1^2 , 0.00 , 0.00 , sd2^2), nrow=nDim, ncol=nDim)

# Now generate the random walk. stepIdx is the step in the walk.
for (stepIdx in 1:(trajLength-1) ) {
