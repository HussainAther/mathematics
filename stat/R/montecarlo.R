library(knitr)
library(rafalib)
library(downloader)
url <- "https://raw.githubusercontent.com/genomicsclass/dagdata/master/inst/extdata/mice_pheno.csv"

# Monte Carlo simulations

set.seed(1)
filename <- "mice_pheno.csv"
if (!file.exists(filename)) download(url,destfile=filename)

library(dplyr)
dat <- read.csv("mice_pheno.csv")
controlPopulation <- filter(dat,Sex == "F" & Diet == "chow") %>%  
  select(Bodyweight) %>% unlist

# Generate t-statistic under null hypothesis for a sample size n.
ttestgenerator <- function(n) {
  #note that here we have a false "high fat" group where we actually
  #sample from the chow or control population. 
  #This is because we are modeling the null.
  cases <- sample(controlPopulation,n)
  controls <- sample(controlPopulation,n)
  tstat <- (mean(cases)-mean(controls)) / 
      sqrt( var(cases)/n + var(controls)/n ) 
  return(tstat)
  }
ttests <- replicate(1000, ttestgenerator(10))
