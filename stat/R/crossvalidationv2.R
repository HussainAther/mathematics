library(knitr)
library(tissuesGeneExpression)
data(tissuesGeneExpression)

# Implementation of cross-validation (CV)

# Drop tissues without many samples.
table(tissue)
ind <- which(tissue != "placenta")
y <- tissue[ind]
X <- t( e[,ind] )

# K-nearest (k nearest) neighbors for classification (knn)
library(class)
pred <- knn(train =  X, test = X, cl=y, k=5)
mean(y != pred)

library(caret)
set.seed(1)
idx <- createFolds(y, k=10)
sapply(idx, length)

library(rafalib)
mypar()
Xsmall <- cmdscale(dist(X))
plot(Xsmall,col=as.fumeric(y))
legend("topleft",levels(factor(y)),fill=seq_along(levels(factor(y))))
pred <- knn(train=Xsmall[ -idx[[1]] , ], test=Xsmall[ idx[[1]], ], cl=y[ -idx[[1]] ], k=5)
table(true=y[ idx[[1]] ], pred)
mean(y[ idx[[1]] ] != pred)

for (i in 1:10) {
    pred <- knn(train=Xsmall[ -idx[[i]] , ], test=Xsmall[ idx[[i]], ], cl=y[ -idx[[i]] ], k=5)
    print(paste0(i,") error rate: ", round(mean(y[ idx[[i]] ] != pred),3)))
}

set.seed(1)
ks <- 1:12
res <- sapply(ks, function(k) {
    # try out each version of k from 1 to 12
    res.k <- sapply(seq_along(idx), function(i) {
        # loop over each of the 10 cross-validation folds
        # predict the held-out samples using k nearest neighbors
        pred <- knn(train=Xsmall[ -idx[[i]], ],
                    test=Xsmall[ idx[[i]], ],
                    cl=y[ -idx[[i]] ], k = k)
        # the ratio of misclassified samples
        mean(y[ idx[[i]] ] != pred)
    })
    # average over the 10 folds
    mean(res.k)
})

Xsmall <- cmdscale(dist(X),k=5)
set.seed(1)
ks <- 1:12
res <- sapply(ks, function(k) {
  res.k <- sapply(seq_along(idx), function(i) {
    pred <- knn(train=Xsmall[ -idx[[i]], ],
                test=Xsmall[ idx[[i]], ],
                cl=y[ -idx[[i]] ], k = k)
    mean(y[ idx[[i]] ] != pred)
  })
  mean(res.k)
})
plot(ks, res, type="o",ylim=c(0,0.20),ylab="misclassification error")
