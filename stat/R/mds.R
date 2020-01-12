library(knitr)
library(rafalib)
library(tissuesGeneExpression)

# Multi-dimensional scaling for gene expression

data(tissuesGeneExpression)
colind <- tissue%in%c("kidney","colon","liver")
mat <- e[,colind]
group <- factor(tissue[colind])
dim(mat)

