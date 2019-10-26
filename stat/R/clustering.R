"Hierarchical Cluster Analysis"
library(tidyverse) # data manipulation
library(cluster) # clustering algorithms
library(factoextra) # clustering visualization
library(dendextend) # for comparing two dendrograms
df <- USArrests
df <- na.omit(df)

