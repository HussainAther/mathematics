"Discriminant analysis and other linear classification models."
library(AppliedPredictiveModeling)
set.seed(100)
reduceCovMat <- cov(training[, reducedSet])
"Eliminate linear combinations using trim.matrix."
library(subselect)
trimmingResults <- trim.matrix(reducedCovMat)
"Identify predictors."
fullCovMat <- cov(training[, fullSet])
fullSetResults <- trim.matrix(fullCovMat)
"May choose what to exclude using this function."
fullSetREsults$names.discarded
