# Bayesian updating of beliefs about the bias of a coin. 
# The prior and posterior distributions indicate probability masses at discrete candidate values of θ.
# Theta is the vector of candidate values for the parameter theta.

# nThetaVals is the number of candidate theta values.
nThetaVals = 3

# Now make the vector of theta values:
Theta = seq(from = 1/(nThetaVals+1), to = nThetaVals/(nThetaVals+1), by = 1/(nThetaVals+1))

# pTheta is the vector of prior probabilities on the theta values.
pTheta = pmin( Theta , 1-Theta ) # Makes a triangular belief distribution.
pTheta = pTheta / sum( pTheta ) # Makes sure that beliefs sum to 1.

# Specify the data.
Data = c(1,1,1,0,0,0,0,0,0,0,0,0) 
nHeads = sum( Data == 1 )
nTails = sum( Data == 0 )

# Compute the likelihood of the data for each value of theta:
pDataGivenTheta = ThetaˆnHeads * (1-Theta)^nTails

# Compute the posterior:
pData = sum( pDataGivenTheta * pTheta )
pThetaGivenData = pDataGivenTheta * pTheta / pData # Bayes' rule

# Plot the results.
windows(7,10) # create window of specified width,height inches.
layout( matrix( c( 1,2,3 ) ,nrow=3 ,ncol=1 ,byrow=FALSE ) ) # 3x1 panels
par(mar=c(3,3,1,0)) # number of margin lines: bottom,left,top,right
par(mgp=c(2,1,0)) # which margin lines to use for labels
par(mai=c(0.5,0.5,0.3,0.1)) # margin size in inches: bottom,left,top,right
