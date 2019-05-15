" "
c_light <- c("#DCBCBC")
c_light_highlight <- c("#C79999")
c_mid <- c("#B97C7C")
c_mid_highlight <- c("#A25050")
c_dark <- c("#8F2727")
c_dark_highlight <- c("#7C0000")

x <- seq(-10, 10, 0.001)
plot(x, dcauchy(x, location = 0, scale = 1), type="l", col=c_dark_highlight, lwd=2,
     main="", xlab="x", ylab="Probability Density", yaxt='n')
