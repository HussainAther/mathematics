"Estimate joint probability density for the volumes of the amygdala and acc (anterior
cingulate cotrtex)."
library(np)
df <- read.csv(file="data/n90_pol.csv", header=TRUE, sep=",")
bw <- npudensbw(df)
    fhat <- npudens(bw)
pdfy <- function(df) {
  result <- sapply(df, function(b) integrate(function(a) pdfxy(a, b), 0, 2)$value)
  return(result)
}
