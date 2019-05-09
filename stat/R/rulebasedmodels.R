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
