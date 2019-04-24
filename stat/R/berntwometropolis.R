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
}
