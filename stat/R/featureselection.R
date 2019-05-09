"Feature feature selection."
library(AppliedPredictiveModeling)
library(caret)
library(klaR)
library(leaps)
library(MASS)
library(pROC)
library(rms)
library(stats)
data(AlzheimerDisease)
predictors$E2 <- predictors$E3 < predictors$E4 <- 0
predictors$E2[grepl("2", predictors$Genotype)] <- 1
predictors$E3[grepl("3", predictors$Genotype)] <- 1
predictors$E4[grepl("4", predictors$Genotype)] <- 1
