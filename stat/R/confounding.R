library(knitr)

# Surrogate variables and batch effects 

# Admission data from Berkeley 1973 showed more men 
# were being admitted than women: 44\% men admitted 
# compared to 30\% women!

# confounding
datadir="http://www.biostat.jhsph.edu/bstcourse/bio751/data"
dat=read.csv(file.path(datadir,"admissions.csv"))
dat$total=dat$Percent*dat$Number/100

# percent men get in
sum(dat$total[dat$Gender==1]/sum(dat$Number[dat$Gender==1]))
# percent women get in
sum(dat$total[dat$Gender==0]/sum(dat$Number[dat$Gender==0]))
