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
"A test had been conducted with the purpose of investigating if people recollect pleasant 
memories associated with a word earlier than some unpleasant memory related with the same 
word. The word is flashed on the screen and the time an individual takes to respond via 
the keyboard is recorded for both types of the memories."
"Tukey's (tukey) five number inter-difference, Bowley-Tukey (bowley tukey) measure of skewness"
# For memory recall times (Dunn and Master (1982))
data(memory)
lapply(memory,fivenum)
lapply(memory,mad)
lapply(memory,IQR)
fnid <- function(x) diff(fivenum(x)) # difference of fivenum
lapply(memory,fnid)
fnid_pleasant <- fnid(memory$Pleasant.memory)
fnid_unpleasant <- fnid(memory$Unpleasant.memory)
btskew_pleasant <- (fnid_pleasant[3]-fnid_pleasant[2])/(fnid_pleasant[3]+fnid_pleasant[2]) 
btskew_unpleasant <- (fnid_unpleasant[3]-fnid_unpleasant[2])/(fnid_unpleasant[3]+fnid_unpleasant[2])
btskew_pleasant; btskew_unpleasant

"The Youden-Beale Experiment. We need to compare here if the two virus extracts have a varying effect on the 
tobacco leaf or not. First, the boxplot is generated without the notches for yb data.frame using the boxplot 
function. The median for Preparation_1 certainly appears higher than for Preparation_2. Thus, we are tempted to 
check whether the medians for the two preparations are significantly different with the notched boxplot. Now, 
the boxplot is generated to produce the notches with the option notch=TRUE. Appropriate headers for a figure 
are specified with the title function. Most importantly, we have used a powerful graphical technique of R 
through par, which is useful in setting graphical parameters. Here, mfrow indicates that we need a multi-
row figure with one row and two columns."
