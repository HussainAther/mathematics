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
"Train samples using estimated parameters with index argument to identify the samples."
ctrl <- trainControl(method = "LGOCV", summaryFunction = twoClassSummary,
                     classProbs = TRUE, index = list(TrainSet = pre2008, 
                     savePredictions = TRUE))
"Logistic regression (logistic)."
modelFit <- glm(Class ~ Dat, data = training[pre2008,],
                family = binomial)
modelFit
"Use the probability of a successful grant."
successProb <- 1 - predict(modelFit, newdata = data.frame(Day = c(10, 150, 300, 350)),
                           type = "response")
successProb
"Add nonlinear term for the day of the year."
daySquaredModel <- glm(Class ~ Day + I(Day^2), data = training[pre2008,],
                       family = binomial)
daySquaredModel
"Regression modeling Strategies (regression strategies) package."
library(rms)
rcsFit <- lrm(Class ~ rcs(Day), data = training[pre2008,])
rscFit
"Predict."
dayProfile <- Predict(rcsFit, Day = 0:365, fun = function(x) - x)
plot(dayProfile, ylab = "Log Odds")
"Augment the data using predictor groups with squared day variable."
training$Day2 <- training$Day^2
fullSet <- c(fullSet, "Day2")
reducedSet <- c(reducedSet, "Day2")
library(caret)
set.seed(100)
lrFull <- train(training[, fullSet], y = training$Class,
                method = "glm", metric = "ROC", trControl = ctrl)
lrFull
"Use a smaler predictor set."
lrReduced <- train(training[, reducedSet], y = training$Class,
                   method = "glm", metric = "ROC", trcontrol = ctrl)
lrReduced
"Linear discriminant analysis."
library(MASS)
grantPreProcess <- preProcess(training[pre2008, reducedSet])
grantPreProcess
scaledPre2008 <- predict(grantPreProcess, newdata = training[pre2008, reducedSet])
scaled2008HoldOut <- predict(grantPreProcess, newdata = training[-pre2008, reducedSet])
ldaModel <- lda(x = scaledPre2008, grouping = training$Class[pre2008])
ldaHoldOutPredictions <- predict(ldaModel, scaled2008HoldOut)
ldaFit1 <- train(x = training[, reducedSet], y = training$Class,
                 method = "lda", preProc = c("center", "scale"),
                 metric = "ROC", trControl = ctrl)
lidFit1
ldaTestClasses <- predict(ldaFit1, newdata = testing[, reducedSet])
ldaTestProbs <- predict(ldaFit1, newdata = testing[, reducedSet], type = "prob")
"Partial least squares discriminant analysis (partial) PLS pls."
plsdaModel <- plsda(x = training[pre2008, reducedSet],
                    y = training[pre2008, "Class"],
                    scale = TRUE, probMethod = "Bayes", ncomp 4)
plsPred <- predict(plsdaModel, newdata = training[-pre2008, reducedSet], type = "prob")
"We evaluate the first ten PlS components."
plsFit2 <- train(x = training[, reducedSet], y = training$Class,
                 method = "pls", tuneGrid = expand.grid(.ncomp = 1:10),
                 preProc = c("center", "scale"), metric = "ROC", trControl = ctrl)
plsImpGrant <- varImp(plsFit2, scale = FALSE)
plsImpGrant
plot(plsImpGrant, top = 20, scales = list(y = list(cex = .05)))
"Penalized models (penalized)"
library(glmnet)
glmnetModel < glmnet(x = as.matrix(training[, fullSet]),
                     y = training$Class, family = "binomial")
"Compute predictions for three difference levels of regularization."
predict(glmnetModel, newx = as.matrix(training[1:5, fullSet]), s = c(.05, .1, .2), 
        type = "class")
predict(glmnetModel, newx = as.matrix(training[1:5, fullSet]), s = c(.05, .1, .2), 
        type = "nonzero")
glmnGrid <- expand.grid(.alpha = c(0, .1, .2, .4, .6, .8, 1), 
                        .lambda = seq(.01, .2, length = 40))
glmTuned <- train(training[, fullSet], y = training$Class,
                  method = "glmnet", tuneGrid = glmnGrid,
                  preProc = c("center", "scale"), metric = "ROC",
                  trControl = ctrl)
