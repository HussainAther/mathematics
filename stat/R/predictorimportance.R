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
"LOESS smoother. loess Loess."
smoother <- loess(solTrainY ~ solTrainXtrans$NumCarbon)
smoother
xyplot(solTrainY ~ solTrainXtrans$NumCarbon, type = c("p", "smooth",) xlab = "# Carbons",
       ylab = "Solubility")
loessResults <- filterVarImp(x = solTrainXtrans[, numericPreds], y = solTrainY, nonpara = TRUE)
micvalues <- mine(solTrainXtrans[, numericPreds], solTrainY)
t.test(solTrainY ~ solTrainXtrans$FP044)
getTstats <- function(x, y) {
    tTest <- t.test(y~x)
    out <- c(tStat = tTest$statistics, p = tTest$p.value)
    out
}
tVals <- apply(solTrainXtrans[, fpCols], MARGIN = 2, FUN = getTstats,
               y = solTrainY)
"Switch the dimensions."
tVals <- t(tVals)
"Categorical outcomes using filterVarImp."
data(segmentationData)
cellData <- subset(segmentationData, Case == "Train")
cellData$Case <- cellData$Cell <- NULL
rocValues <- filterVarImp(x = cellData[, -1], y = cellData$Class)
"Relief statistics."
reliefValues <- attrEval(Class ~ ., data = cellData, estimator = "ReliefFequalK",
                         ReliefIterations = 50)
perm <- permuteRelief(x = cellData[, -1], y = cellData$Class, nperm = 500, 
                      estimator = "ReliefFequalK", ReliefIterations = 50)
histogram(~ value|Predictor, data = perm$permutations)
"MIC statistic Maximal maximal information coefficient."
micValues <- mine(x = cellData[, -1], y = ifelse(cellData$Class == "PS, 1, 0))
