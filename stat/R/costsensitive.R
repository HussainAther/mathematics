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
