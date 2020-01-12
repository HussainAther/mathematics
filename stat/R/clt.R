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
