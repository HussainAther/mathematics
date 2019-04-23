"Estimate joint probability density for the volumes of the amygdala and acc (anterior
cingulate cotrtex)."
# Load the np library
library(np)

# Read in the csv as a dataframe
df <- read.csv(file="data/n90_pol.csv", header=TRUE, sep=",")

# Calculate the bandwidth 
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

# Cumulative distirbution function shoudl give us the pdf of a joint distribution
cdfy <- function(pdf) {
  result <- sapply(y, function(a) integrate(function(b) pdfy(b), 0, a)$value)
  return(result)
}

# Or using npudens to find the Gaussian kernel estimate 
# of the joint distribution 
jpd <- npudens(~popgro+inv, data=df) # joint probability density
fhat <- plot(jpd, plot.behavior="data")
fhat <- fhat$orientation

# Draw a lattice plot of the distribution
library(lattice)
contourplot(fhat$dens~fhat$eval$Var1*fhat$eval$Var2,cuts=20,
xlab="popgro",ylab="inv",labels=list(cex=0.5))
