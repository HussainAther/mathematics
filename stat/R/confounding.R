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

# chi-square (chi square) test
indexes<-list(1:6,7:12)
tab <- matrix(NA,2,2,dimnames=list(c("males","females"),c("accepted","rejected")))
for(i in 1:2){
  ind<-indexes[[i]]
  tab[i,1]<- sum(dat[ind,2]*dat[ind,3]/100)
  tab[i,2] <- sum(dat[ind,2]*(1-dat[ind,3]/100))
}
tab <- round(tab)
tab
print(chisq.test(tab)$p.val)
