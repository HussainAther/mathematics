library(dplyr)
library(knitr)
library(rafalib)
dat <- read.csv("femaleMiceWeights.csv")

# T-test (ttest t test) in practice

control <- filter(dat,Diet=="chow") %>% select(Bodyweight) %>% unlist
treatment <- filter(dat,Diet=="hf") %>% select(Bodyweight) %>% unlist

diff <- mean(treatment) - mean(control)
sd(control)/sqrt(length(control))
se <- sqrt( 
    var(treatment)/length(treatment) + 
    var(control)/length(control) 
    )
tstat <- diff/se 

righttail <- 1 - pnorm(abs(tstat)) 
lefttail <- pnorm(-abs(tstat))
pval <- lefttail + righttail
print(pval)

# qqplot
mypar(1,2)
qqnorm(treatment)
qqline(treatment,col=2)
qqnorm(control)
qqline(control,col=2)

t.test(treatment, control)
result <- t.test(treatment,control)
result$p.value
