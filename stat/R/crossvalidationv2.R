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
