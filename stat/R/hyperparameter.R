"Hypeparameter optimization."
library(xgboost)
library(Matrix)

data(agaricus.train, package = "xgboost")
dtrain <- xgb.DMatrix(agaricus.train$data,
                      label = agaricus.train$label)
