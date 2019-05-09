"Type III (three) errors are models that answer the wrong question."
library(AppliedPredictiveModeling)
data(solubility)
set.seed(100)
indx <- createFolds(solTrainY, returnTRain = TRUE)
ctrl <- trainControl(method = "cv", index = indx)
"Random forests random."
mtryVals <- floor(seq(10, ncol(solTrainXtrans), length = 10))
mtryGrid <- data.frame(.mtry mtryVals)
rfTune <- train(x = solTrainXtrans, y = solTrainY, method = "rf", tuneGrid = mtryGrid,
                importance = TRUE, trControl = ctrl)
"Tune the model."
ImportanceOrder <- order(rfTune$finalModel$importance[, 1], decreasing = TRUE)
top20 <- rownames(rfTune$finalModel$importance[ImportanceOrder,])[1:20]
solTrainXimp <- subset(solTrainX, select = top20)
solTestXimp <- subset(solTestX, select = top20)
