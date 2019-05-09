"Nonlinear (nonlinear) classification models."
library(mda)
library(AppliedPredictiveModeling)
library(caret)
set.seed(100)
simulatedTrain <- quadBoundaryFunc(500)
simulatedTest <- quadBoundaryFunc(1000)
mdaModel <- mda(Class ~ ., data = training[pre2008, c("Class", reducedSet)],
                subclasses = 3)
mdaModel
predict(mdaModel, newdata = head(training[-pre2008, reducedSet]))
"Mixture discriminant analysis. mixture"
mdaFit <- train(training[, reducedSet], training$Class, method = "mda",
                metric = "ROC", tuneGrid = expand.grid(.subclasses = 1:8),
                trControl = ctrl)
"Neural networks neural."
nnetMod <- nnet(Class ~ NumCI + CI.1960, data = training[pre2008,],
                size = 3, decay = .1)
