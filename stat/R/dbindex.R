# Davies–Bouldin index 
dbindex <- function(clustering, centers, data, metric="euclidean", stand=FALSE)
 {
   clusters <- sort(unique(clustering))
   ds <- as.matrix(daisy(rbind(data, centers), metric, stand))
   to.center <- sapply(clusters, function(d) mean(ds[clustering==d,nrow(data)+d]))
   between.centers <- ds[(nrow(data)+1):(nrow(data)+length(clusters)),
                          (nrow(data)+1):(nrow(data)+length(clusters))]
   diag(between.centers) <- NA
   'dimnames<-'(outer(clusters, clusters, Vectorize(function(d1, d2)
                                                   (to.center[d1]+to.center[d2])/
                                                    between.centers[d1,d2])),
               list(clusters, clusters))
}
