"Algorithms for predictor importance."
library(AppliedPredictiveModeling)
library(caret)
library(CORElearn)
library(minerva)
library(pROV)
library(randomForest)
data(solubility)
cor(solTrainXtrans$NumCarbon, solTrainY)
fpCols <- grepl("FP", names(solTrainXtrans))
numericPreds <- names(solTRainXtrans)[!fpCols]
corrValues <- apply(solTrainXtrans[, numericPreds], MARGIN =2,
                    FUN = function(x, y) cor(x, y),
                    y = solTrainY)
