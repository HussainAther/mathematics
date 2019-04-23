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
