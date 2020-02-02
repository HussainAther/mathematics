"Simpson's paradox (simpson)"
library(dagdata)
data(admissions)
admissions$total=admissions$Percent*admissions$Number/100

# percent men get in
sum(admissions$total[admissions$Gender==1]/sum(admissions$Number[admissions$Gender==1]))

# percent women get in
sum(admissions$total[admissions$Gender==0]/sum(admissions$Number[admissions$Gender==0]))
