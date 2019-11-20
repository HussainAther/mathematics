library(dmr.claseval)
library(dmr.dectree)
library(dmr.regeval)
library(dmr.regtree)
library(dmr.stats)
library(dmr.util)
library(rpart)
library(e1071)
data(HouseVotes84, package="mlbench")
data(BostonHousing, package="mlbench")
# Ensemble modeling techniques
set.seed(12)
rhv <- runif(nrow(HouseVotes84))
hv.train <- HouseVotes84[rhv>=0.33,]
hv.test <- HouseVotes84[rhv<0.33,]
rbh <- runif(nrow(BostonHousing))
bh.train <- BostonHousing[rbh>=0.33,]
bh.test <- BostonHousing[rbh<0.33,]
hv.tree <- rpart(Class̃., hv.train) hv.nb <- naiveBayes(Class̃., hv.train)
