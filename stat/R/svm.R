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
  
