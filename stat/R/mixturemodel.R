snoqualmie <- scan("http://www.stat.washington.edu/peter/book.data/set1",skip=1)
snoq <- snoqualmie[snoqualmie > 0]
summary(snoq)
library(mixtools)
snoq.k2 <- normalmixEM(snoq,k=2,maxit=100,epsilon=0.01)
