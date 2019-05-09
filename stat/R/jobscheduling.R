"Job scheduling problem in high-performance computing (high performance HPC hpc)."
library(AppliedPredictiveModeling)
data(HPC)
set.seed(100)
inTrain <- createDataPartition(schedulingData$Class, p = .8, list = FALSE)
schedulingData$NumPending <- schedulingData$NumPending + 1
trainData <- schedulingData[inTrain,]
testData <- schedulingData[-inTrain,]
cost <- function(pred, obs) {
    isNA <- is.na(pred)
    if(!all(isNA)) {
        pred <- pred[!isNA]
        obs <- obs[!isNA]
        if(any(pred == "VF" & obs == "L"))
            cost[pred == "L" & obs == "VF"] <- 10
        if(any(pred =="F" & obs == "L"))
            cost[pred == "F" & obs == "L"] <- 5
        if(any(pred == "F" & obs == "M"))
            cost[pred == "F" & obs == "M"] <- 5
        if(any(pred == "VF" & obs == "M"))
            cost[pred == "VF" & obs == "M"] <- 5
        out <- mean(cost)
    } else out <- NA
}
costSummary <- function(data, lev = NULL, model = NULL) {
    if (is.character(data$obs)) data$obs <- factor(data$obs, levels = lev)
    c(postResample(data[, "pred"], data[, "obs"]),
      Cost = cost(data[, "pred"], data[, "obs"))
}
"Control object"
ctrl <- trainControl(method = "repeatedcv", repeats = 5, summaryFunction = costSummary)
"Matrix representation of the costs (matrix)."
costMatrix <- ifelse(diag(4) == 1, 0, 1)
costMatrix[1, 4] <- 10
costMatrix[1, 3] <- 5
costMatrix[2, 4] <- 5
costMatrix[2, 4] <- 5
rownames(costMatrix) <- levels(trainData$Class) 
colnames(costMatrix) <- levels(trainData$Class)
costMatrix
"Model formula to log transform several of the predictors."
modForm <- as.formula(Class ~ Protocol + log10(Compounds) + log10(InputFields) + 
                      log10(Iterations) + log10(NumPending + Hour + Day)
"Weighted model function." 
rpFitCost <- train(x = trainData[, predictors], y = trainData$Class,
                   method = "rpart", metric = "Cost", maximize = FALSE,
                   tuneLength = 20, parms = list(loss = t(costMatrix)),
                   trControl = ctrl)
"C5.0)
C50Cost <- train(x = trainData[, predictors], y = trainData$Class,
                 method = "C5.0", metric = "Cost", mazimize = FALSE,
                 costs = costMatrix, tuneGrid = expand.grid(.trials = c(1, (1:10*10),
                                                            .model = "tree", 
                                                            .winnow = c(TRUE, FALSE)),
                 trControl = ctrl)
"Cost-sensitive bagged trees."
rpCost <- function(x, y) {
    costMatrix <- ifelse(diag(4) == 1, 0, 1)
    costMatrix[4, 1] <- 10
    costMatrix[3, 1] <- 5
    costMatrix[4, 2] <- 5
    costMatrix[3, 2] <- 5
    tmp <- x
    tmp$y <- y
    rpart(y ~ data = tmp, control = rpart.control(cp = 0),
          parms = list(loss = costMatrix))
}
rpPredict <- function(object, x) predict(object, x)
rpAgg <- function(x, type = "class") { 
    pooled <- x[[1]] * NA
    n <- nrow(pooled)
    classes <- colnames(pooled)
    for (i in 1:ncol(pooled)) {
        tmp <- lapply(x, function(y, col) y[, col], col = i)
        tmp <- do.call("rbind", tmp)
        pooled[, i] <- apply(tmp, 2, median) 
    }
    pooled <- apply(pooled, 1, functino(x) x/sum(x))
    if (n != nrow(pooled)) pooled <- t(pooled)
    out <- factor(classes[apply(pooled, 1, which.max)], levels = classes)
    out
}
rpCostBag <- train(trainData[, predictors], trainData$Class,
                   "bag", B = 50, bagControl = bagControl(fit = rpCost,
                   predict = rpPredict, aggregate = rpAgg, downSample = FALSE), 
                   trControl = ctrl)
"Weighted SVM svm"
svmRFitCost <- train(modForm, data = trainData, method = "svmRadial",
                     metric = "Cost", maximize = FALSE, preProc = c("center", "scale"),
                     class.weights = c(VF = 1, F = 1, M = 5, L = 10), tuneLength = 15,
                     trControl = ctrl)
"Confusion confusion matrix."
confusionMatrix(rpFitCost, norm = "none")
