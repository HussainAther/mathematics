snoqualmie <- scan("http://www.stat.washington.edu/peter/book.data/set1",skip=1)
snoq <- snoqualmie[snoqualmie > 0]
summary(snoq)
library(mixtools)
snoq.k2 <- normalmixEM(snoq, k=2, maxit=100, epsilon=0.01)
plot(hist(snoq, breaks=101), col="grey", border="grey", freq=FALSE,
    xlab="Precipitation (1/100 inch)", main="Precipitation in Snoqualmie Falls")
lines(density(snoq), lty="dashed")
