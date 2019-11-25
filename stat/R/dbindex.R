# Davies–Bouldin index 
dbindex <- function(clustering, centers, data, metric="euclidean", stand=FALSE)
 {
   clusters <- sort(unique(clustering))
   ds <- as.matrix(daisy(rbind(data, centers), metric, stand))

