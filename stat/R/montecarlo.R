library(knitr)
library(rafalib)
library(downloader)
url <- "https://raw.githubusercontent.com/genomicsclass/dagdata/master/inst/extdata/mice_pheno.csv"

# Monte Carlo simulations

set.seed(1)
filename <- "mice_pheno.csv"
if (!file.exists(filename)) download(url,destfile=filename)
