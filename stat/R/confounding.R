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

# percent admissions by major
y=cbind(dat[1:6,c(1,3)],dat[7:12,3])
colnames(y)[2:3]=c("Male","Female")
y

# Simpson's paradox
y=cbind(dat[1:6,5],dat[7:12,5])
y=sweep(y,2,colSums(y),"/")*100
x=rowMeans(cbind(dat[1:6,3],dat[7:12,3]))
matplot(x,y,xlab="percent that gets in the major",ylab="percent that applies to major",col=c("blue","red"),cex=1.5)
legend("topleft",c("Male","Female"),col=c("blue","red"),pch=c("1","2"),box.lty=0)
