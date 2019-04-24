# Use this program as a template for experimenting with the Metropolis
# algorithm applied to two parameters called theta1,theta2 defined on the

# Load MASS
library(MASS)

# Define the likelihood function.
# The input argument is a vector: theta = c(theta1, theta2)
likelihood = function(theta) {
