# Bayesian updating of beliefs about the bias of a coin. 
# The prior and posterior distributions indicate probability masses at discrete candidate values of θ.
# Theta is the vector of candidate values for the parameter theta.
# nThetaVals is the number of candidate theta values.
# To produce the examples in the book, set nThetaVals to either 3 of 63.
nThetaVals = 3
# Now make the vector of theta values:
Theta = seq(from = 1/(nThetaVals+1), to = nThetaVals/(nThetaVals+1), by = 1/(nThetaVals+1))
# pTheta is the vector of prior probabilities on the theta values.
pTheta = pmin( Theta , 1-Theta ) # Makes a triangular belief distribution.
pTheta = pTheta / sum( pTheta ) # Makes sure that beliefs sum to 1.
