library(downloader)
library(knitr)

# Procedure of computing a p-value ofr each gene and calling
# genes with p-values smaller than it significant.

filename <- "femaleControlsPopulation.csv"

set.seed(1)
population = unlist( read.csv("femaleControlsPopulation.csv") )
alpha <- 0.05
N <- 12
m <- 10000
pvals <- replicate(m,{
    control = sample(population,N)
    treatment = sample(population,N)
    t.test(treatment,control)$p.value
})

# Get R
sum(pvals < 0.05)alpha <- 0.05
N <- 12
m <- 10000
p0 <- 0.90 # 10% of diets work, 90% don't
m0 <- m*p0
m1 <- m-m0
nullHypothesis <- c( rep(TRUE,m0), rep(FALSE,m1))
delta <- set.seed(1)
calls <- sapply(1:m, function(i){
  control <- sample(population,N)
  treatment <- sample(population,N)
  if(!nullHypothesis[i]) treatment <- treatment + delta
  ifelse( t.test(treatment,control)$p.value < alpha, 
          "Called Significant",
          "Not Called Significant")
})
null_hypothesis <- factor( nullHypothesis, levels=c("TRUE","FALSE"))
table(null_hypothesis,calls)
B <- 10 # number of simulations
VandS <- replicate(B,{
  calls <- sapply(1:m, function(i){
    control <- sample(population,N)
    treatment <- sample(population,N)
    if(!nullHypothesis[i]) treatment <- treatment + delta
    t.test(treatment,control)$p.val < alpha
  })
  cat("V =",sum(nullHypothesis & calls), "S =",sum(!nullHypothesis & calls),"\n")
  c(sum(nullHypothesis & calls),sum(!nullHypothesis & calls))
  })

# Vectorize by using a matrix.

library(genefilter) # rowttests is here
set.seed(1)

# Define groups to be used with rowttests.
g <- factor( c(rep(0,N),rep(1,N)) )
B <- 1000 # number of simulations
Qs <- replicate(B,{
  # matrix with control data (rows are tests, columns are mice)
  controls <- matrix(sample(population, N*m, replace=TRUE),nrow=m)
  
  # matrix with control data (rows are tests, columns are mice)
  treatments <-  matrix(sample(population, N*m, replace=TRUE),nrow=m)
  
  # add effect to 10% of them
  treatments[which(!nullHypothesis),]<-treatments[which(!nullHypothesis),]+delta
  
  # combine to form one matrix
  dat <- cbind(controls,treatments)
  
 calls <- rowttests(dat,g)$p.value < alpha
 R=sum(calls)
 Q=ifelse(R>0,sum(nullHypothesis & calls)/R,0)
 return(Q)
})

# Control FDR (false discovery rate).
library(rafalib)
mypar(1,1)
hist(Qs)
FDR=mean(Qs)
print(FDR)

set.seed(1)
controls <- matrix(sample(population, N*m, replace=TRUE),nrow=m)
treatments <-  matrix(sample(population, N*m, replace=TRUE),nrow=m)
treatments[which(!nullHypothesis),]<-treatments[which(!nullHypothesis),]+delta
dat <- cbind(controls,treatments)
pvals <- rowttests(dat,g)$p.value 

# Make histogram.
h <- hist(pvals,breaks=seq(0,1,0.05))
polygon(c(0,0.05,0.05,0),c(0,0,h$counts[1],h$counts[1]),col="grey")
abline(h=m0/20)
h <- hist(pvals,breaks=seq(0,1,0.01))
polygon(c(0,0.01,0.01,0),c(0,0,h$counts[1],h$counts[1]),col="grey")
abline(h=m0/100)
