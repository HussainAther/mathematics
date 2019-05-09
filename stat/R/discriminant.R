"Discriminant analysis and other linear classification models."
library(AppliedPredictiveModeling)
set.seed(100)
reduceCovMat <- cov(training[, reducedSet])
"Eliminate linear combinations using trim.matrix."
library(subselect)
trimmingResults <- trim.matrix(reducedCovMat)
