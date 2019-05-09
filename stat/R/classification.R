"Measuring performance in classification models."
"quadBoundaryFunc generates predictors and outcomes."
library(AppliedPredictiveModeling)
set.seed(100)
simulatedTrain <- quadBoundaryFunc(500)
simulatedTest <- quadBoundaryFunc(1000)
"Random forest and quadratic discriminant models fit to data.
library(randomForest)
rfModel <- randomForest(class ~ X1 + X2,
                        data = simulatedTrain,
                        ntree = 2000)
library(MASS)
qdaModel <- qda(class ~ X1 + X2, data = simulatedTrain)
