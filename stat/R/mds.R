library(knitr)
library(rafalib)
library(tissuesGeneExpression)

# Multi-dimensional scaling for gene expression

data(tissuesGeneExpression)
colind <- tissue%in%c("kidney","colon","liver")
mat <- e[,colind]
group <- factor(tissue[colind])
dim(mat)

# single value decomposition
s <- svd(mat-rowMeans(mat))
PC1 <- s$d[1]*s$v[,1]
PC2 <- s$d[2]*s$v[,2]
mypar(1,1)
plot(PC1,PC2,pch=21,bg=as.numeric(group))
legend("bottomright",levels(group),col=seq(along=levels(group)),pch=15,cex=1.5)

# Plot the variance to show the components separated.
plot(s$d^2/sum(s$d^2))

# Show the rest.
PC3 <- s$d[3]*s$v[,3]
PC4 <- s$d[4]*s$v[,4]
mypar(1,1)
plot(PC3,PC4,pch=21,bg=as.numeric(group))
legend("bottomright",levels(group),col=seq(along=levels(group)),pch=15,cex=1.5)

# Classic multidimensional scaling (cmdscale)
d <- dist(t(mat))
mds <- cmdscale(d)
mypar()
plot(mds[,1],mds[,2],bg=as.numeric(group),pch=21,
     xlab="First dimension",ylab="Second dimension")
legend("bottomleft",levels(group),col=seq(along=levels(group)),pch=15)

mypar(1,2)
for(i in 1:2){
    plot(mds[,i],s$d[i]*s$v[,i],main=paste("PC",i))
    b = ifelse( cor(mds[,i],s$v[,i]) > 0, 1, -1)
    abline(0,b) ##b is 1 or -1 depending on the arbitrary sign "flip"
}
