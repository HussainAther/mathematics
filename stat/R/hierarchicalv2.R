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
i.stdm <- std.all(Species~., i.train) 
i.std.train <- predict.std(i.stdm, i.train) 
i.std.test <- predict.std(i.stdm, i.test)
g.std <- std.all(Type~., g.train) 
g.std.train <- predict.std(g.stdm, g.train) 
g.std.test <- predict.std(g.stdm, g.test)
dg.l4 <- lapply(1:8, function(i)
                     {
                       d <- list(i)
                       attr(d, "members") <- 1
                       attr(d, "height") <- 0
                       attr(d, "leaf") <- TRUE
                       attr(d, "label") <- i
                       'class<-'(d, "dendrogram")
})
dgmerge <- function(dg, i1, i2)
{
  d <- list(dg[[i1]], dg[[i2]])
  attr(d, "members") <- attr(d[[1]], "members")+attr(d[[2]], "members")
  attr(d, "height") <- 1+max(attr(d[[1]], "height"), attr(d[[2]], "height"))
  attr(d, "leaf") <- FALSE
  lab <- if (is.null(attr(d[[1]], "edgetext"))) "label" else "edgetext"
  attr(d, "edgetext") <- paste(attr(d[[1]], lab), attr(d[[2]], lab), sep="+")
  'class<-'(d, "dendrogram")
}
dg.l3 <- lapply(seq(1, length(dg.l4)-1, 2), function(i) dgmerge(dg.l4, i, i+1))
dg.l2 <- lapply(seq(1, length(dg.l3)-1, 2), function(i) dgmerge(dg.l3, i, i+1))
dg.l1 <- lapply(seq(1, length(dg.l2)-1, 2), function(i) dgmerge(dg.l2, i, i+1))
plot(dg.l1[[1]], center=TRUE)

# Agglomerative hierarchical clustering
ahc <- function(data, linkf=ahc.size, diss=euc.dist, bottom=1:nrow(data))
  {
    clid <- function(d) # hclust-compatible cluster id scheme
    { if (d>length(bottom.clusters)) d-length(bottom.clusters) else -d }
    dm <- as.matrix(dissmat(data, diss)) # instance dissimilarity matrix for linkage
    bottom.clusters <- unique(bottom) # bottom-level clusters
    clustering <- bottom # current cluster assignment
    clusters <- bottom.clusters # current set of clusters
    merge <- NULL # merge matrix
    height <- NULL # height vector
    order <- NULL # order vector
    links <- outer(1:length(clusters), 1:length(clusters),
                   Vectorize(function(i1, i2)
                             if (i1<i2)
                               linkf(clustering, clusters[i1], clusters[i2], data,
                                     diss, dm) 
