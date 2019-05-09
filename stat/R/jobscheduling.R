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
