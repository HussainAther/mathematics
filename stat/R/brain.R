"Estimate joint probability density for the volumes of the amygdala and acc (anterior
cingulate cotrtex)."
# Read in the csv as a dataframe
df <- read.csv(file="data/n90_pol.csv", header=TRUE, sep=",")

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

# Load the np library
library(np)

# Calculate the bandwidth 
bw <- npudensbw(df)
    fhat <- npudens(bw)

# Joint probability density
jpd <- npudens(bw, data=df) 
fhat <- plot(jpd, plot.behavior="data")
fhat <- fhat$orientation

# Draw a lattice plot of the distribution
library(lattice)
contourplot(fhat$dens~fhat$eval$Var1*fhat$eval$Var2,cuts=20,
xlab="popgro",ylab="inv",labels=list(cex=0.5))

# Bootstrap with 95 % CI (confidence intervals Confidence) for regression coefficients
# function to obtain regression weights 
bs <- function(formula, data, indices) {
  d <- data[indices,] # allows boot to select sample 
  fit <- lm(formula, data=d)
  return(coef(fit)) 
} 

# Bootstrap (bootstrap) with 1000 replications
results <- boot(data=df, statistic=bs, 
   R=1000, formula=mpg~wt+disp)

# Plot
results
plot(results, index=1) # intercept 
plot(results, index=2) # wt 
plot(results, index=3) # disp 

# get 95% confidence intervals 
boot.ci(results, type="bca", index=1) # intercept 
boot.ci(results, type="bca", index=2) # wt 
boot.ci(results, type="bca", index=3) # disp

# Kernel conditional density estimation
npcdens(bw, data=df)
