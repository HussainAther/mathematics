library(knitr)
library(dplyr)
dat <- read.csv("femaleMiceWeights.csv")

# T-test (ttest t test) in practice

control <- filter(dat,Diet=="chow") %>% select(Bodyweight) %>% unlist
treatment <- filter(dat,Diet=="hf") %>% select(Bodyweight) %>% unlist

diff <- mean(treatment) - mean(control)
