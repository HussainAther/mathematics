# Bayesian updating for Bernoulli likelihood and beta prior.
BernBeta = function(priorShape, dataVec, credMass=.95, saveGraph=F) {
# priorShape is a vector of parameter values for the prior beta distribution,
# dataVec is a vector of 1's and 0's of the data,
# credMass is the probability mass of the equal tailed credible interval
# Return postShape, a vector of parameter avlues for the posterior beta distribution,
# and create a three-panel graph of prior, likelihood, and posterior with highest posterior
# density interval.
if (length(priorShape) != 2) {
    stop("priorShape must have two components.") }
if (any(priorShape <= 0)) { 
    stop("priorShape components must be positive.") }
if (any(dataVec != 1 & dataVec != 0)) {
    stop("dataVec must bea vector of 1s and 0s.") } 
if (credMass <= 0 | credMass >= 1.0) {
    stop("credMass must be between 0 and 1.") }

# Rename the prior shape parameters, for convenience.
a = priorShape[1]
b = priorShape[2]

# Create summary values of the data.
z = sum(dataVec==1) # Number of 1s in dataVec
N = length(dataVec) # Number of flips in dataVec

# Compute the posterior shape parameters.
postShape = c(a+z, b+N-z)

# Compute the evidence, p(D).
pData = beta(z+a, N-z+b) / beta(a, b)

# Determine the limits of the highest density interval.
# This uses a home-grown function called HDIofICDF.
source("HDIofICDF.R")
hpdLim = HDIofICDF(qbeta, shape1=postShape[1], shape2=postShape[2])

# Plot 
# Construct a grid of theta values, used for graphing
binwidth = 0.005 # Arbitrary small value for comb on Theta.
Theta = seq(from = binwidth/2, to = 1-(binwidth/2), by = binwidth)

# Compute the prior at each value of theta.
pTheta=dbeta(Theta,a,b)

# Compute the likelihood of the data at each value of theta.
pDataGivenTheta = Theta^z * (1-Theta)^(N-z)

# Compute the posterior at each value of theta.
pThetaGivenData = dbeta(Theta , a+z , b+N-z)

# Open a window with three panels.
windows(7,10)
layout(matrix(c(1, 2, 3), nrow=3, ncol=1, byrow=FALSE)) # 3x1 panels
par(mar=c(3,3,1,0), mgp=c(2,1,0), mai=c(0.5,0.5,0.3,0.1)) # margin specs
maxY = max(c(pTheta, pThetaGivenData)) # max y for plotting

# Plot the prior.
plot(Theta, pTheta, type="l", lwd=3, xlim=c(0,1), ylim=c(0,maxY), cex.axis=1.2,
     xlab=bquote(theta), ylab=bquote(p(theta)), cex.lab=1.5, main="Prior", cex.main=1.5)
if(a>b){textx=0;textadj=c(0,1)}
else {textx = 1 ; textadj = c(1,1)}
text(textx, 1.0*max(pThetaGivenData), bquote("beta("*theta*"|"*.(a)*","*.(b)*")"),
    cex=2.0, adj=textadj)
