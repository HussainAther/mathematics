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
