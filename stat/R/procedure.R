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
