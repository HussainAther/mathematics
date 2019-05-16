"Hypeparameter optimization."
library(xgboost)
library(Matrix)

data(agaricus.train, package = "xgboost")
dtrain <- xgb.DMatrix(agaricus.train$data,
                      label = agaricus.train$label)
cv_folds <- KFold(agaricus.train$label, nfolds = 5,
                  stratified = TRUE, seed = 0)
"Bayesian optimization."
xgb_cv_bayes <- function(max_depth, min_child_weight, subsample) {
  cv <- xgb.cv(params = list(booster = "gbtree", eta = 0.01,
                             max_depth = max_depth,
                             min_child_weight = min_child_weight,
                             subsample = subsample, colsample_bytree = 0.3,
                             lambda = 1, alpha = 0,
                             objective = "binary:logistic",
                             eval_metric = "auc"),
               data = dtrain, nround = 100,
               folds = cv_folds, prediction = TRUE, showsd = TRUE,
               early_stopping_rounds = 5, maximize = TRUE, verbose = 0)
