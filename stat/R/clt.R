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
sd_hf <- popsd(hfPopulation)
sd_control <- popsd(controlPopulation)

N <- 12
hf <- sample(hfPopulation, 12)
control <- sample(controlPopulation, 12)

# Use qqplots to see how well the CLT works for this data.
Ns <- c(3,12,25,50)
B <- 10000 #number of simulations
res <-  sapply(Ns,function(n) {
    replicate(B,mean(sample(hfPopulation,n))-mean(sample(controlPopulation,n)))
})
mypar(2,2)
for (i in seq(along=Ns)) {
  titleavg <- signif(mean(res[,i]),3)
  titlesd <- signif(popsd(res[,i]),3)
  title <- paste0("N=",Ns[i]," Avg=",titleavg," SD=",titlesd)
  qqnorm(res[,i],main=title)
  qqline(res[,i],col=2)
}
