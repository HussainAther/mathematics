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

# dataset for plots
kmf.plot <- function(a1, a2) { 2*a1-3*a2+4 }
kmdat.plot <- 'names<-'(expand.grid(seq(1, 5, 0.05), seq(1, 5, 0.05)), c("a1", "a2"))
kmdat.plot$f <- kmf.plot(kmdat.plot$a1, kmdat.plot$a2)
kmdat.plot$c <- as.factor(ustep(kmdat.plot$f))

# datasets for parameter estimation examples
kmg<-function(a1, a2, a3, a4) { a1^2+2*a^2-a3^2-2*a4^2+2*a1-3*a2+2*a3-3*a4+1 } 
kmf <- function(a1, a2, a3, a4) { 3*a1+4*a2-2*a3+2*a4-3 }
kmdat <- data.frame(a1=runif(400, min=1, max=5), a2=runif(400, min=1, max=5),
                    a3=runif(400, min=1, max=5), a4=runif(400, min=1, max=5))
kmdat$g <- kmg(kmdat$a1, kmdat$a2, kmdat$a3, kmdat$a4)
kmdat$c <- as.factor(ustep(kmdat$g))
kmdat$f <- kmf(kmdat$a1, kmdat$a2, kmdat$a3, kmdat$a4)

kmdat.train <- kmdat[1:200,]
kmdat.test <- kmdat[201:400,]

# linearly separable training and test subsets 
kmdat.ls <- linsep.sub(c~a1+a2+a3+a4, kmdat) 
kmdat.train.ls <- kmdat[1:200,][kmdat.ls[1:200],] 
kmdat.test.ls <- kmdat[201:400,][kmdat.ls[201:400],] 
