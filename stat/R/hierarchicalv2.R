library(dmr.dissim)
library(dmr.trans)
library(cluster)
data(weathercl, package="dmr.data")
data(iris)
data(Glass, package="mlbench")

set.seed(12)
ri <- runif(nrow(iris))
i.train <- iris[ri>=0.33,]
i.test <- iris[ri<0.33,]
rg <- runif(nrow(Glass))
g.train <- Glass[rg>=0.33,]
g.test <- Glass[rg<0.33,]
wcl.std <- predict.std(std.all(.~., weathercl), weathercl)
i.stdm <- std.all(Species̃., i.train) 
i.std.train <- predict.std(i.stdm, i.train) 
i.std.test <- predict.std(i.stdm, i.test)
    
