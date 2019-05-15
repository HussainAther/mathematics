"The Cauchy density function enjoys a notorious reputation in mathematics, 
serving as a common counterexample to identify incomplete proofs in probability 
theory. At the same time it has also been a consistent source of frustration 
for statistical computation. We use the formula for the Cauchy (cauchy) distribution
probability density function."

c_light <- c("#DCBCBC")
c_light_highlight <- c("#C79999")
c_mid <- c("#B97C7C")
c_mid_highlight <- c("#A25050")
c_dark <- c("#8F2727")
c_dark_highlight <- c("#7C0000")

x <- seq(-10, 10, 0.001)
plot(x, dcauchy(x, location = 0, scale = 1), type="l", col=c_dark_highlight, lwd=2,
     main="", xlab="x", ylab="Probability Density", yaxt="n")

"Looking at the quantile distribution we see the tails in high probabilty."

x <- seq(0, 1, 0.001)
plot(x, qcauchy(x, location = 0, scale = 1), type="l", col=c_dark_highlight, lwd=2,
     main="", xlab="Probability", ylab="Quantile")
lines(x, qnorm(x, 0, 1), type="l", col=c_light_highlight, lwd=2)

text(x=0.9, y=250, labels="Cauchy", col=c_dark_highlight)
text(x=0.9, y=-50, labels="Normal", col=c_light_highlight)
