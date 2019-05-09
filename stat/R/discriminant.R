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
