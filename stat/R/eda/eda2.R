# Exploratory data analysis (eda)
library(LearnEDA)
library(e1071)
library(sfsmisc)
library(qcc)
library(aplpack)
library(RSADBE)
library(ACSWR)

"The Youden-Beale Experiment. We need to compare here if the two virus extracts have a varying effect on the 
tobacco leaf or not. First, the boxplot is generated without the notches for yb data.frame using the boxplot 
function. The median for Preparation_1 certainly appears higher than for Preparation_2. Thus, we are tempted to 
check whether the medians for the two preparations are significantly different with the notched boxplot. Now, 
the boxplot is generated to produce the notches with the option notch=TRUE. Appropriate headers for a figure 
are specified with the title function. Most importantly, we have used a powerful graphical technique of R 
through par, which is useful in setting graphical parameters. Here, mfrow indicates that we need a multi-
row figure with one row and two columns."

par(mfrow=c(1,2))
yb <- read.table("/.../youden.csv",header=T,sep=",")
data(yb)
title("A: Boxplot for Youden-Beale Data")
boxplot(yb,notch=TRUE)
title("B: Notched Boxplots Now")
