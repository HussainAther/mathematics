"Hierarchical Cluster Analysis"
library(tidyverse) # data manipulation
library(cluster) # clustering algorithms
library(factoextra) # clustering visualization
library(dendextend) # for comparing two dendrograms
df <- USArrests
df <- na.omit(df)
df <- scale(df)
"Agglomerative Hierarchical Clustering"
# Dissimilarity matrix
d <- dist(df, method = "euclidean")
# Hierarchical clustering using Complete Linkage
hc1 <- hclust(d, method = "complete" )
# Plot the obtained dendrogram
plot(hc1, cex = 0.6, hang = -1)
# Compute with agnes
hc2 <- agnes(df, method = "complete")
# Agglomerative coefficient
hc2$ac
