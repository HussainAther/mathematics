"Cost-sensitive (cost sensitive) training."
library(DWD)
library(caret)
library(C50)
library(DMwR)
library(kernlab)
library(pROC)
library(rpart)
data(ticdata)
recodeLevels <- function(x) {
    x <- as.numeric(x)
    x <- gsub(" ", "0", format(as.numeric(x)))
    factor(x)
}
isOrdered <- unlist(lapply(ticdata, is.ordered))
isFactor <- unlist(lapply(ticdata, is.factor))
convertCols <- names(isOdrered)[isOrdered | isFactor]
for(i in convertCols) ticdata[, i] <- recodeLevels(ticdata[, i])
ticdata$CARAVAN <- factor(as.character(ticdata$CARAVAN), levels = rev(levels(ticdata$CARAVAN)))
"Use stratified random sampling for training set."
split1 <- createDataPartition(ticdata$CARAVAN, p = .7)[[1]]
other <- ticdata[-split1, ]
training <- ticdata[split1,]
"Evaluation and test sets."
split2 <- createDataPartition(other$CARAVAN, p = 1/3)[[1]]
evaluation <- other[split2,]
testing <- other[-split2,]
"Determine predictors."
predictors <- names(training)[names(training) != "CARAVAN"]
"Random forest."
trainingInd <- data.frame(model.matrix(CARAVAN ~ ., data = training))[, -1]
evaluationInd <- data.frame(model.matrix(CARAVAN ~ ., data = evaluation))[, -1]
testingInd <- data.frae(model.matrix(CARAVAN ~ ., data = testing))[, -1]
"Add the outcome into the data set."
trainingInd$CARAVAN <- training$CARAVAN
evaluationInd$CARAVAN <- evaluation$CARAVAN
testingInd$CARAVAN <- testing$CARAVAN
"Determine a predictor set without highly spare and unbalanced distributions."
isNZV <- nearZeroVar(trainingInd)
noNZVSet <- names(trainingInd)[-isNZV]
"Performance measures."
fiveStats <- function(...) c(twoClassSummary(...), defaultSummary(...))
fourStats <- function(data, lev = levels(data$obs), model = NULL) {
    accKap <- postResample(data[, "pred"], data[, "obs")
    out <- c(accKapp, sensitivity(data[, "pred"], data[, "obs"], lev[1]),
                      specificity(data[, "pred"], data[, "obs"], lev[2]))
    names(out)[3:4] <- c("Sens", "Spec")
    out
}
"Two control functions for scenarios in which class probabilities can be created
and cannot."
ctrl <- trainControl(method = "cv", classProbs = TRUE", summaryFunction = fiveStats,
                     verboseIter = TRUE)
ctrlNoProb <- ctrl
ctrlNoProb$summaryFunction <- fourStats
ctrlNoProb$classProbs <- FALSE
"Three baseline models."
"Random field specification."
rfFit <- train(CARAVAN ~ ., data = trainingInd, method = "rf",
               trControl = ctrl, ntree = 1500, tuneLength = 5, metric = "ROC")
"Logistic regression."
lrFit <- train(CARAVAN ~ ., data = trainingInd[, noNZVSet], method = "glm",
               trControl = ctrl, metric = "ROC")
"Flexible discriminant analysis."	
fdaFit <- train(CARAVAN ~ ., data = training, method = "fda", tuneGrid = data.frame(.degree = 1,
                nprune = 1:25), metric = "ROC", trControl = ctrl)
"House predictions."
evalResults <- data.frame(CARAVAN = evaluations$CARAVAN)
evalResults$RF <- predict(rfFit, newdata = evaluationInd, type = "prob")[, 1]
evalResults$FDA <- predict(fdaFit, newdata = evaluation[, predictors], type = "prob")[, 1]
evalResults$LogReg <- predict(lrFit, newdata = evaluationInd[, noNZVSet], type = "prob")[, 1]
"ROC roc and lift curves."
rfROC <- roc(evalResults$CARAVAN, evalResults$RF, levels = rev(levels(evalResults$CARAVAN)))
labs <- c(RF = "Random Forest", LogReg = "Logistic Regression", FDA = "FDA (MARS)")
lift1 <- lift(CARAVAN ~ RF + LogReg + FDA, data = evalResults, labels = labs)
rfROC 
"Alternative cutoffs"
rfThresh <- coords(rfROC, x = "best", best.method = "closest.topleft")
rfThresh
"Predict new classes."
newValue <- factor(ifelse(evalResults$RF > rfThres, "insurance", "noinsurance"),
                   levels = levels(evalResults$CARAVAN))
"Sampling methods."
upSampledTrain <- upSample(x = training[, predictors], y = training$CARAVAN, yname = "CARAVAN")
smoteTrain <- SMOTE(CARAVAN ~ ., data = training)
"Cost-sensitive training."
sigma <- sigest(CARAVAN ~ ., data = trainingInd[, noNZVSet], frac = .75)
names(sigma) <- NULL
svmGRid <- data.frame(.sigma = sigma[2], .C = 2^seq(-6, 1, length = 15))
SVMwts <- train(CARAVAN ~ ., data = trainingInd[, noNZVSet], method = "svmRadial",
                tuneGRid = svmGrid, preProc = c("center", "scale"), class.weights = c(insurance = 18, 
                noinsurance = 1), metric = "Sens", trControl = ctrlNoProb)
SVMwts
"Use cost matrices matrix"
costMatric <- matrix(c(0, 1, 20, 0), ncol = 2)
rownames(costMatrix) <- levels(training$CARAVAN)
colnames(costMatrix) <- levels(training$CARAVAN)
costMatrix
"C5.0"
c5Matrix <- matrix(c(0, 20, 1, 0), ncol = 2)
rownames(c5matrix) <- levels(training$CARAVAN)
colnames(c5matrix) <- levels(training$CARAVAN)
c5Matrix
C5Cost <- train(x = training[, predictors], y = training$CARAVAN,
                method = "C5.0", metric = "Kappa", cost = c5Matrix,
                trControl = ctrlNoProb)
