"Feature feature selection."
library(AppliedPredictiveModeling)
library(caret)
library(klaR)
library(leaps)
library(MASS)
library(pROC)
library(rms)
library(stats)
set.seed(100)
data(AlzheimerDisease)
predictors$E2 <- predictors$E3 < predictors$E4 <- 0
predictors$E2[grepl("2", predictors$Genotype)] <- 1
predictors$E3[grepl("3", predictors$Genotype)] <- 1
predictors$E4[grepl("4", predictors$Genotype)] <- 1
"Stratified sampling."
split <- createDataPartition(diagnosis, p = .8, list = FALSE)
"Combine into one data frame."
adData <- predictors
adData$Class <- diagnosis
training <- adData[split,]
testing <- adData[-split,]
"Save a vector of predictor variable names."
predVars <- names(adData[!(names(adData) %in% c("Class", "Genotype"))]
"Area under ROC curve, sensitivity, specificity, accuracy, and Kappa."
fiveStats <- function(...) c(twoClassSummary(...), defaultSummary(...))
"Resampling data sets for all models."
index <- createMultiFolds(training$Class, times = 5)
"Vector of subset sizes to evaluate."
varSeq <- seq(1, length(predVars)-1, by = 2)
"Logistic regression."
initial <- glm(Class ~ tau + BEGF + E4 + IL_3, data = training, family = binomial)
stepAIC(initial, direction = "both")
"Recursive feature elimination (recursive)."
str(rfFuncs)
newRF <- rfFuncs
newRF$summary <- fiveStats
"Control function."
ctrl <- rfeControl(method = "repeatedcv", repeats = 5, verbose = TRUE,
                   functions = newRF, index = index)
"RFE procedure." 
rfRFE <- rfe(x = training[, predVars], y = training$Class, sizes = varSeq,
             metric = "ROC", rfeControl = ctrl, ntree = 1000)
rfFRE
predict(rfRFE, head(testing))
"SVM svm"
svmFuncs <- caretFuncs
svmFuncs$summary <- fivestats
ctrl <- rfeControl(method = "repeatedcv", repeats = 5, verbose = TRUE,
                   functions = svmFuncs, index = index)
svmRFE <- rfe(x = training[, predVars], y = training$Class, sizes = varSeq, metric = "ROC",
              rfeControl = ctrl, method = "svmRadial", tuneLength = 12, preProc = c("center", "scale"),
              trControl = trainControl(method = "cv", verboseIter = FALSE, classProbs = TRUE))
svmRFE
