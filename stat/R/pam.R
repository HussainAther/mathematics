library(dmr.claseval)
library(dmr.stats)
library(dmr.trans)
library(dmr.util)
library(cluster)
data(iris)
set.seed(12)
ri <- runif(nrow(iris))
i.train <- iris[ri>=0.33,]
i.test <- iris[ri<0.33,]

# PAM clustering models

i.stdm <- std.all(Species̃., i.train) i.std.train <- predict.std(i.stdm, i.train) i.std.test <- predict.std(i.stdm, i.test)

i.pam2.euc <- pam(i.std.train[,-5], 2, metric="euclidean")
i.pam3.euc <- pam(i.std.train[,-5], 3, metric="euclidean")
i.pam5.euc <- pam(i.std.train[,-5], 5, metric="euclidean")
i.pam7.euc <- pam(i.std.train[,-5], 7, metric="euclidean")
i.pam2.man <- pam(i.std.train[,-5], 2, metric="manhattan")
i.pam3.man <- pam(i.std.train[,-5], 3, metric="manhattan")
i.pam5.man <- pam(i.std.train[,-5], 5, metric="manhattan")
i.pam7.man <- pam(i.std.train[,-5], 7, metric="manhattan")

predict.pam <- function(model, data, dmf=daisy, ...)
  {
    k.centers.assign(model$medoids, data,
                     function(x1, x2) dmf(rbind(x1, x2), ...))
}
i.pam2.euc.pred <- predict(i.pam2.euc, i.std.test[,-5])
i.pam3.euc.pred <- predict(i.pam3.euc, i.std.test[,-5])
i.pam5.euc.pred <- predict(i.pam5.euc, i.std.test[,-5])
i.pam7.euc.pred <- predict(i.pam7.euc, i.std.test[,-5])
i.pam2.man.pred <- predict(i.pam2.man, i.std.test[,-5])
i.pam3.man.pred <- predict(i.pam3.man, i.std.test[,-5])
i.pam5.man.pred <- predict(i.pam5.man, i.std.test[,-5])
i.pam7.man.pred <- predict(i.pam7.man, i.std.test[,-5])

diameter <- function(clustering, data, metric="euclidean", stand=FALSE)
{
  clusters <- sort(unique(clustering))
  dm <- as.matrix(daisy(data, metric, stand))
  'names<-'(sapply(clusters, function(d) max(dm[clustering==d,clustering==d])),
clusters)
}
diameter(i.pam2.euc$clustering, i.std.train[,-5])
diameter(i.pam3.euc$clustering, i.std.train[,-5])
diameter(i.pam5.euc$clustering, i.std.train[,-5])
diameter(i.pam7.euc$clustering, i.std.train[,-5])
diameter(i.pam2.man$clustering, i.std.train[,-5], metric="manhattan")
diameter(i.pam3.man$clustering, i.std.train[,-5], metric="manhattan")
diameter(i.pam5.man$clustering, i.std.train[,-5], metric="manhattan")
diameter(i.pam7.man$clustering, i.std.train[,-5], metric="manhattan")
diameter(i.pam2.euc.pred, i.std.test[,-5])
diameter(i.pam3.euc.pred, i.std.test[,-5])
diameter(i.pam5.euc.pred, i.std.test[,-5])
diameter(i.pam7.euc.pred, i.std.test[,-5])
diameter(i.pam2.man.pred, i.std.test[,-5], metric="manhattan")
diameter(i.pam3.man.pred, i.std.test[,-5], metric="manhattan")
diameter(i.pam5.man.pred, i.std.test[,-5], metric="manhattan")
diameter(i.pam7.man.pred, i.std.test[,-5], metric="manhattan")

# Rand index calculation
randindex <- function(clustering, classes)
{ 
  mean(outer(1:length(clustering), 1:length(classes),
             function(i, j)
             ifelse(i!=j,
                    clustering[i]==clustering[j] & classes[i]==classes[j]  |
                    clustering[i]!=clustering[j] & classes[i]!=classes[j, NA)),
       na.rm=TRUE)
}
randindex(i.pam2.euc$clustering, i.std.train[,5])
randindex(i.pam3.euc$clustering, i.std.train[,5])
randindex(i.pam5.euc$clustering, i.std.train[,5])
randindex(i.pam7.euc$clustering, i.std.train[,5])
randindex(i.pam2.man$clustering, i.std.train[,5])
randindex(i.pam3.man$clustering, i.std.train[,5])
randindex(i.pam5.man$clustering, i.std.train[,5])
randindex(i.pam7.man$clustering, i.std.train[,5])
randindex(i.pam2.man$clustering, i.std.test[,5])
randindex(i.pam3.man$clustering, i.std.test[,5])
randindex(i.pam5.man$clustering, i.std.test[,5])
randindex(i.pam7.man$clustering, i.std.test[,5])

separation <- function(clustering, data, metric="euclidean", stand=FALSE)
{
  clusters <- sort(unique(clustering))
  dm <- as.matrix(daisy(data, metric, stand))
  'names<-'(sapply(clusters, function(d) min(dm[clustering==d,clustering!=d])),
clusters)
}
separation(i.pam2.euc$clustering, i.std.train[,-5])
separation(i.pam3.euc$clustering, i.std.train[,-5])
separation(i.pam5.euc$clustering, i.std.train[,-5])
separation(i.pam7.euc$clustering, i.std.train[,-5])
separation(i.pam2.man$clustering, i.std.train[,-5], metric="manhattan")
separation(i.pam3.man$clustering, i.std.train[,-5], metric="manhattan")
separation(i.pam5.man$clustering, i.std.train[,-5], metric="manhattan")
separation(i.pam7.man$clustering, i.std.train[,-5], metric="manhattan")
separation(i.pam2.euc.pred, i.std.test[,-5])
separation(i.pam3.euc.pred, i.std.test[,-5])
separation(i.pam5.euc.pred, i.std.test[,-5])
separation(i.pam7.euc.pred, i.std.test[,-5])
separation(i.pam2.man.pred, i.std.test[,-5], metric="manhattan")
separation(i.pam3.man.pred, i.std.test[,-5], metric="manhattan")
separation(i.pam5.man.pred, i.std.test[,-5], metric="manhattan")
separation(i.pam7.man.pred, i.std.test[,-5], metric="manhattan")

isolation <- function(clustering, data, metric="euclidean", stand=FALSE)
{
  clusters <- sort(unique(clustering))
  dm <- as.matrix(daisy(data, metric, stand))
  diam <- diameter(clustering, data, metric, stand)
  sep <- separation(clustering, data, metric, stand)
  is <- sapply(clusters,
               function(d)
               if (all(apply(dm[clustering==d,clustering==d,drop=FALSE], 1, max)<
                         apply(dm[clustering==d,clustering!=d,drop=FALSE], 1, min)))
                 "L*"
               else if (diam[d]<sep[d])
"L" else
                 "no")
  ‘names<-‘(factor(is, levels=c("no", "L", "L*")), clusters)
}
isolation(i.pam2.euc$clustering, i.std.train[,-5])
isolation(i.pam3.euc$clustering, i.std.train[,-5])
isolation(i.pam5.euc$clustering, i.std.train[,-5])
isolation(i.pam7.euc$clustering, i.std.train[,-5])
isolation(i.pam2.man$clustering, i.std.train[,-5], metric="manhattan")
isolation(i.pam3.man$clustering, i.std.train[,-5], metric="manhattan")
isolation(i.pam5.man$clustering, i.std.train[,-5], metric="manhattan")
isolation(i.pam7.man$clustering, i.std.train[,-5], metric="manhattan")
isolation(i.pam2.euc.pred, i.std.test[,-5])
isolation(i.pam3.euc.pred, i.std.test[,-5])
isolation(i.pam5.euc.pred, i.std.test[,-5])
isolation(i.pam7.euc.pred, i.std.test[,-5])
isolation(i.pam2.man.pred, i.std.test[,-5], metric="manhattan")
isolation(i.pam3.man.pred, i.std.test[,-5], metric="manhattan")
isolation(i.pam5.man.pred, i.std.test[,-5], metric="manhattan")
isolation(i.pam7.man.pred, i.std.test[,-5], metric="manhattan")
