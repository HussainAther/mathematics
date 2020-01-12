library(dplyr)
library(knitr)
library(rafalib)

# Central limit theorem

dat <- read.csv("mice_pheno.csv") 
controlPopulation <- filter(dat,Sex == "F" & Diet == "chow") %>%  
  select(Bodyweight) %>% unlist
hfPopulation <- filter(dat,Sex == "F" & Diet == "hf") %>%  
  select(Bodyweight) %>% unlist

mypar(1,2)
hist(hfPopulation)
hist(controlPopulation)

mypar(1,2)
qqnorm(hfPopulation)
qqline(hfPopulation)
qqnorm(controlPopulation)
qqline(controlPopulation)

set.seed(1) 
library(downloader)
url <- "https://raw.githubusercontent.com/genomicsclass/dagdata/master/inst/extdata/mice_pheno.csv"
filename <- "mice_pheno.csv"
if (!file.exists(filename)) download(url,destfile=filename)

dat <- read.csv("mice_pheno.csv") 
head(dat)
