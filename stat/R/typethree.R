"Type III (three) errors are models that answer the wrong question."
library(AppliedPredictiveModeling)
data(solubility)
set.seed(100)
indx <- createFolds(solTrainY, returnTRain = TRUE)
ctrl <- trainControl(method = "cv", index = indx)
