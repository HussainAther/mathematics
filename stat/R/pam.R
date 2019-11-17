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

i.stdm <- std.all(Species̃., i.train) i.std.train <- predict.std(i.stdm, i.train) i.std.test <- predict.std(i.stdm, i.test)

i.pam2.euc <- pam(i.std.train[,-5], 2, metric="euclidean")
i.pam3.euc <- pam(i.std.train[,-5], 3, metric="euclidean")
i.pam5.euc <- pam(i.std.train[,-5], 5, metric="euclidean")
i.pam7.euc <- pam(i.std.train[,-5], 7, metric="euclidean")
i.pam2.man <- pam(i.std.train[,-5], 2, metric="manhattan")
i.pam3.man <- pam(i.std.train[,-5], 3, metric="manhattan")
i.pam5.man <- pam(i.std.train[,-5], 5, metric="manhattan")
i.pam7.man <- pam(i.std.train[,-5], 7, metric="manhattan")

"Rand index calculation."
randindex <- function(clustering, classes)
{ 
  mean(outer(1:length(clustering), 1:length(classes),
             function(i, j)
             ifelse(i!=j,
                    clustering[i]==clustering[j] & classes[i]==classes[j]  |
                    clustering[i]!=clustering[j] & classes[i]!=classes[j, NA)),
       na.rm=TRUE)
}
# Training set
randindex(i.pam2.euc$clustering, i.std.train[,5])
randindex(i.pam3.euc$clustering, i.std.train[,5])
randindex(i.pam5.euc$clustering, i.std.train[,5])
randindex(i.pam7.euc$clustering, i.std.train[,5])

randindex(i.pam2.man$clustering, i.std.train[,5])
randindex(i.pam3.man$clustering, i.std.train[,5])
randindex(i.pam5.man$clustering, i.std.train[,5])
randindex(i.pam7.man$clustering, i.std.train[,5])

# Test set 
randindex(i.pam2.man$clustering, i.std.test[,5])
randindex(i.pam3.man$clustering, i.std.test[,5])
randindex(i.pam5.man$clustering, i.std.test[,5])
randindex(i.pam7.man$clustering, i.std.test[,5])
