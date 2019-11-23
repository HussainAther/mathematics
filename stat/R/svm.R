library(dmr.claseval)
library(dmr.linclas)
library(dmr.regeval)
library(dmr.util)
library(lattice)
library(quadprog)
library(kernlab)
library(Matrix)
data(PimaIndiansDiabetes, package="mlbench")
data(BostonHousing, package="mlbench")

"""
Kernel support vector machine (svm).
"""

set.seed(12)
rpid <- runif(nrow(PimaIndiansDiabetes))
pid.train <- PimaIndiansDiabetes[rpid>=0.33,]
pid.test <- PimaIndiansDiabetes[rpid<0.33,]
 
rbh <- runif(nrow(BostonHousing))
bh.train <- BostonHousing[rbh>=0.33,-4]
bh.test <- BostonHousing[rbh<0.33,-4]

pid.stdm <- std.all(diabetes~., pid.train) 
pid.std.train <- predict.std(pid.stdm, pid.train) 
pid.std.test <- predict.std(pid.stdm, pid.test)
bh.stdm <- std.all(medv~., bh.train) 
bh.std.train <- predict.std(bh.stdm, bh.train) 
bh.std.test <- predict.std(bh.stdm, bh.test) 
