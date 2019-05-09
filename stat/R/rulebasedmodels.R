"Rule-based models. Build single classification trees. Use predictors for the data
to model classes for groupes categories."
library(rpart)
library(mda)
library(AppliedPredictiveModeling)
library(caret)
set.seed(100)
cartModel <- rpart(factorForm, data = training[pre2008,])
rpart(Class ~ NumCI + Weekday, data = training[pre2008,])
library(RWeka)
J48(Class ~ NumCI + Weekday, data = training[pre2008,])
library(C50)
C5tree <- C5.0(Class ~ NumCI + Weekday, data = training[pre2008,])
C5tree
summary(C5tree)
"Fit the grouped category model for CART."
rpartGrouped <- train(x = training[, factorPredictors], y = training$Class,
                      method = "rpart", tuneLength = 30, metric = "ROC",
                      trControl = ctrl)
PART(Class ~ NumCI + Weekday, data = training[pre2008,])
C5rules <- C5.0(Class ~ NumCI + Weekday, data = training[pre2008,], rules = TRUE)
C5Rules
summary(C5rules)
"Bagged bagged trees."
bagging(Class ~ Weekday + NumCI, data = training[pre2008,])
"Random random forest."
library(randomForest)
randomForest(Class ~ NumCI + Weekday, data = training[pre2008,])
"Boosted boosted trees."
library(gbm)
forGBM <- training
forGBM$Class <- ifelse(forGBM$Class == "successful", 1, 0)
gbmModel <- gbm(Class ~ NumCI + Weekday, data = forGBM[pre2008,],
                distribution = "bernoulli", interaction.depth = 9,
                n.trees = 1400, shrinkage = .01, verbose = FALSE)
gbmPred <- predict(gbmModel, newdata = head(training[-pre2008,]), 
                   type = "response", n.trees = 1400)
gbmPred
gbmClass <- ifelse(gbmPred > .5, "successful", "unsuccessful")
gbmClass <- factor(gbmClass, levels = levels(training$Class)
gbmClass
"Train boosted versions of C5.0."
library(C50)
C5boost <- C5.0(Class ~ NumCI + Weekday, data = training[pre2008,], trials = 10)
C5boost
