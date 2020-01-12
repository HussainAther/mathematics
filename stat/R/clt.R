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
mu_hf <- mean(hfPopulation)
mu_control <- mean(controlPopulation)
print(mu_hf - mu_control)x <- controlPopulation
N <- length(x)
populationvar <- mean((x-mean(x))^2)
identical(var(x), populationvar)
identical(var(x)*(N-1)/N, populationvar)
