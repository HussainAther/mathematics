# Exploratory data analysis (eda)
library(LearnEDA)
library(e1071)
library(sfsmisc)
library(qcc)
library(aplpack)
library(RSADBE)

x <- c(13,17,11,115,12,7,24)
tab <- cbind(order(x),x[order(x)],c(1:7),c(7:1),pmin(c(1:7), c(7:1)))
colnames(tab) <- c("x_label","x_order","Position_from_min", "Position_from_max","depth")

"Tukey's (tukey) five number inter-difference, Bowley-Tukey (bowley tukey) measure of skewness"
# For memory recall times (Dunn and Master (1982))
data(memory)
lapply(memory,fivenum)
