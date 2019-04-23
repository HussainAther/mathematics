"Estimate joint probability density for the volumes of the amygdala and acc (anterior
cingulate cotrtex)."
library(np)
df <- read.csv(file="data/n90_pol.csv", header=TRUE, sep=",")
bw <- npudensbw(df)
    fhat <- npudens(bw)

# Probability distribution function 
pdfxy <- function(x, y) (x^2 * y + x * y^2)/2
pdfxy(df$amygdala, df$acc)

# Integrate over possible x values
pdf <- function(pdfxy) {
  result <- sapply(df, function(b) integrate(function(a) pdfxy(a, b), 0, 2)$value)
  return(result)
}

# Cumulative distirbution function
cdfy <- function(pdf) {
  result <- sapply(y, function(a) integrate(function(b) pdfy(b), 0, a)$value)
  return(result)
}
