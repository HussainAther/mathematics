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
p0 <- 0.90 ##10% of diets work, 90% don't
m0 <- m*p0
m1 <- m-m0
nullHypothesis <- c( rep(TRUE,m0), rep(FALSE,m1))
delta <- 3set.seed(1)
calls <- sapply(1:m, function(i){
  control <- sample(population,N)
  treatment <- sample(population,N)
  if(!nullHypothesis[i]) treatment <- treatment + delta
  ifelse( t.test(treatment,control)$p.value < alpha, 
          "Called Significant",
          "Not Called Significant")
})
