"Simpson's paradox (simpson)"
library(dagdata)
data(admissions)
admissions$total=admissions$Percent*admissions$Number/100
