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

## functional margin of w with respect to instances from data
## using the cvec vector of {-1, 1} class labels
fmarg <- function(w, data, cvec)
{ cvec*predict.par(list(repf=repf.linear, w=w), data) }

## geometric margin of w with respect to instances from data
## using the cvec vector of {-1, 1} class labels
gmarg <- function(w, data, cvec) { fmarg(w, data, cvec)/l2norm(w[-length(w)]) }

## plot separating and b-margin lines for linear threshold classification
## with 2 attributes
plot.margin <- function(w, data, cvec, b=1, add=FALSE,
                        col.sep="black", col.pos="grey70", col.neg="grey30", ...)

{
  # y value corresponding to x on the regression line represented by w
  lry <- function(x, w) {sum(-w[c(1,3)]/w[2]*c(x, 1)) }
if (!add) {
    plot(data[,1][cvec==1], data[,2][cvec==1], col=col.pos,
       xlab="a1", ylab="a2", xlim=range(data[,1]), ylim=range(data[,2]), ...)
    points(data[,1][cvec!=1], data[,2][cvec!=1], col=col.neg, ...)
  }
  lines(range(data[,1]), c(lry(min(data[,1]), w),
                           lry(max(data[,1]), w)), col=col.sep, ...)
  lines(range(data[,1]), c(lry(min(data[,1]), w-c(0, 0, b)),
                           lry(max(data[,1]), w-c(0, 0, b))), col=col.pos, ...)
  lines(range(data[,1]), c(lry(min(data[,1]), w+c(0, 0, b)),
                           lry(max(data[,1]), w+c(0, 0, b))), col=col.neg, ...)
  list(fmargin=min(fmarg(w, data, cvec)), gmargin=min(gmarg(w, data, cvec)))
}

# dataset for margin illustration (skip near-boundary instances from kmdat.plot)
kmdat.m <- kmdat.plot[abs(kmdat.plot$f)>2,c("a1", "a2", "c")]
kmdat.m <- kmdat.m[sample(nrow(kmdat.m), 100),]

# parameter vector for margin demonstration
w.m <- c(1, -2)

# predictions with intercept 0
p0.m <- predict.par(list(repf=repf.linear, w=c(w.m, 0)), kmdat.m[,1:2])

# symmetric-margin intercept
w.m <- c(w.m, -(max(p0.m[kmdat.m$c==0])+min(p0.m[kmdat.m$c==1]))/2)

# minimum functional margin
min(fmarg(w.m, kmdat.m[,1:2], 2*as.num0(kmdat.m$c)-1))

# minimum geometric
min(gmarg(w.m, kmdat.m[,1:2], 2*as.num0(kmdat.m$c)-1))

# scale parameters to get minimum functional margin of 1
w.m <- w.m/min(fmarg(w.m, kmdat.m[,1:2], 2*as.num0(kmdat.m$c)-1))

# minimum functional margin after parameter scaling (1)
min(fmarg(w.m, kmdat.m[,1:2], 2*as.num0(kmdat.m$c)-1))

# minimum geometric margin after parameter scaling (unchanged)
min(gmarg(w.m, kmdat.m[,1:2], 2*as.num0(kmdat.m$c)-1))
plot.margin(w.m, kmdat.m[,1:2], 2*as.num0(kmdat.m$c)-1)
