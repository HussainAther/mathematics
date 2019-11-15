"Fused lasso. For features that can be ordered, look at the spatial structure
information. Fused lasso takes copy number varition for genomic location into 
account for number-basead classifiers."
X <- matrix(0, 70, 100)
for (i in 1:100){
   X[1:70, i] <- rnorm(80, mean=0, sd=0.5)
}


