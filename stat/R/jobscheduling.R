"Job scheduling problem in high-performance computing (high performance HPC hpc)."
library(AppliedPredictiveModeling)
data(HPC)
set.seed(100)
inTrain <- createDataPartition(schedulingData$Class, p = .8, list = FALSE)

