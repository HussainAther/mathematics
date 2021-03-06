"Measuring performance in classification models."
"quadBoundaryFunc generates predictors and outcomes."
library(AppliedPredictiveModeling)
set.seed(100)
simulatedTrain <- quadBoundaryFunc(500)
simulatedTest <- quadBoundaryFunc(1000)
"Random forest and quadratic discriminant models fit to data.
library(randomForest)
rfModel <- randomForest(class ~ X1 + X2,
                        data = simulatedTrain,
                        ntree = 2000)
library(MASS)
qdaModel <- qda(class ~ X1 + X2, data = simulatedTrain)
qdaTrainPred <- predict(qdaModel, simulatedTrain)
qdaTestPred <- predict(qdaModel, simulatedTest)
simulatedTrain$QDAprob <- qdaTrainPred$posterior[, "Class1"]
simulatedTest$QDAprob <- qdaTestPred$posterior[, "Class1"]
"Get the predicted classes and probabilities."
rfTestPred <- predict(rfModel, simulatedTest, type = "prob")
simulatedTest$RFprob <- rfTestPred[, "Class1"]
simulatedTest$RFclass <- predict(rfModel, simulatedTest)
"Compute sensitivity and specificity."
sensitivity(data = simulatedTest$RFclass,
            reference = simulatedTest$class,
            positive = "Class1")
specificity(data = simulatedTest$RFclass,
            reference = simulatedTest$class,
            negative = "Class2")
"We can also predict using the prevalence or prior judgement."
posPredValue(data = simulatedTest$RFclass,
             reference = simulatedTest$class,
             positive = "Class1")
negPredValue(data = simulatedTest$RFclass,
             reference = simulatedTest$class,
             positive = "Class2")
"Change the prevalence manually."
postPredValue(data = simulatedTest$RFclass,
              reference = simulatedTest$class,
              positive = "Class1",
              prevalence = .9) 
"Create a confusion matrix."
confusionMatrix(data = simulatedTest$RFclass,
                reference = simulatedTest$class,
                positive = "Class1")
"Receiving operating characteristic curves (roc ROC receiving)."
library(pROC)
rocCurve <- roc(response = simulatedTest$class,
                predictor = simulatedTest$RFprob,
                lebels = rev(levels(simulatedTest$class)))
auc(rocCurve)
ci.roc(rocCurve)
"Use plot for ROC curve."
plot(rocCurve, legacy.axes = TRUE)
"Use the lift curve."
labs <- c(RFprob = "Random Forest",
          QDAprob = "Quadratic Discriminant Analysis")
liftCurve <- lift(class ~ RFprob + QDAprob, data = simulatedTest,
                  labels = labs)
liftCurve
"Plot two lift curves using a lattice plot."
xyplot(liftCurve,
       auto.key = list(columns = 2,
                       lines = TRUE,
                       points = FALSE))
"Calibration plots."
calCurve <- calibration(class ~ RFprob + QDAprob, data = simulatedTest)
calCurve
xyplot(calCurve, auto.key = list(columns = 2))
"Binomial distribution for generalized linear model (glm GLM binomial)."
sigmoidalCal <- glm(relevel(class, ref = "Class2") ~ QDAprob,
                    data = simulatedTrain,
                    family = binomial)
coef(summary(sigmoidalCal))
"Corrected probabilities using original model and an equation with slope and intercept."
sigmoidProbs <- predict(sigmoidCal,
                        newdata = simulatedTest[,"QDAprob", drop = FALSE],
                        type = "response")
simulatedTest$QDAsigmoid <- sigmoidProbs
"Bayesian approach for calibration by treating the training set class probabilties as 
estimates of the probabilities Pr[X] and Pr[X|Y = C_l]. We use the NaiveBayes."
BayesCal <- NaiveBayes(class ~ QDAprob, data = simulatedTrain, usekernel = TRUE)
BayesProbs <- predict(BayesCal, newdata = simulatedTest[, "QDAprob", drop = FALSE])
simulatedTest$QDABayes <- BayesProbs$posterior[, "Class1"]
calCurve2 <- calibration(class ~ QDAprob + QDABayes + QDAsigmoid, data = simulatedTest)
xyplot(calCurve2)
