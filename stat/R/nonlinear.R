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
nnetMod
predict(nnetMod, newdata = head(testing), type = "class")
nnetGrid <- expand.grid(.size = 1:10, .decay = c(0, .1, 1, 2))
maxSize <- max(nnetGrid$.size)
numWts - 1*(maxSize * (length(reducedSet) + 1) + maxSize + 1)
nnetFit <- train(x = training[, reducedSet], y = training$Class,
                 method = "nnet", metric = "ROC", preProc = c("center", "scale", "spatialSign"),
                 tuneGrid = nnetGrid, trace = FALSE, maxit = 2000, MaxNWts = numWts, trControl = ctrl)
"Flexible flexible discriminant analysis."
library(earth)
fdaModel <- fda(Class ~ Dat + NumCI, data = training[pre2008,], method = earth)
summary(fdaModel$fit)
predict(fdaModel, head(training[-pre2008,]))
coef(fdaModel)
"Support vector machines svm SVM support."
sigmaRangeReduced <- sigest(as.matrix(training[, reducedSet]))
svmRGridReduced <- expand.grid(.sigma = sigmaRangeReduced[1],
                               .C = 2^(seq(-4,4)))
svmRModel <- train(training[, reducedSet], training$Class,
                   method = "svmRadial", metric = "ROC",
                   preProc = c("center", "scale"),
                   tuneGrid = svmRGridReduced, fit = FALSE, 
                   trControl = ctrl)
svmRModel
library(kernlab)
predict(svmRModel, newdata = head(training[-pre2008, reducedSet]))
"K-nearest neighbors knn KNN K nearest neighbors k."
knnFit <- train(training[, reducedSet[, training$Class,
                method = "knn", metric = "ROC", preProc = c("center", "scale"),
                tuneGrid = data.frame(.k = c(4*(0:5)+1, 20*(1:5)+1, 50*(2:9)+1)),
                trControl = ctrl)
