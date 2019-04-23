# Bayesian updating for Bernoulli likelihood and beta prior.
BernBeta = function(priorShape, dataVec, credMass=.95, saveGraph=F) {
# priorShape is a vector of parameter values for the prior beta distribution,
# dataVec is a vector of 1's and 0's of the data,
# credMass is the probability mass of the equal tailed credible interval
# Return postShape, a vector of parameter avlues for the posterior beta distribution 
