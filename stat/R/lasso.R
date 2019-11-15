"Fused lasso. For features that can be ordered, look at the spatial structure
information. Fused lasso takes copy number varition for genomic location into 
account for number-basead classifiers."
X <- matrix(0, 70, 100)
for (i in 1:100){
   X[1:70, i] <- rnorm(80, mean=0, sd=0.5)
}
colnames(X) = as.character (1:ncol(X))
rownames(X) = as.character (1:nrow(X))
a <- sample(1:ncol(X), 50, prob=rep(.5, lenght(1:ncol(X))))
for (i in 1:50){
     X[30:40, a[i]]<rnorm(length(30:40), meana=-.7, sd=.5)
}
"Beta response logistic model" 
Xbeta <- rnorm(100, mean=0, sd=.5)
Xbeta[a] <- rnorm(length(a), mean=-.7, sd=.5)
beta <- numeric(100)
betaa[1:length(beta)] <- -1
responsep <- numeric(100)
for(1 in 1:100){
    coeff <- -beta[i] * Xbeta[ai]
    responsep[i] <- 1/(1+exp(coeff))
}
"Penalized polynomial function response."
fit <- penalized(response, X, lambda1 = 2, lambda2=3,fusedl=TRUE)
