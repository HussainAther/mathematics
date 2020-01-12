library(knitr)
library(rafalib)

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

# data for plot
mypar()
makematrix<-function(x,m,addx=0,addy=0){
  n<-ceiling(length(x)/m)
  expand.grid(1:n+addx,addy+1:m)[seq(along=x),] 
}
males<- sapply(1:6,function(i){
  tot=dat[i,2]
  p=dat[i,3]/100
  x=rep(c(0,1),round(tot*c(1-p,p)))
})
allmales<-Reduce(c,males)
females<- sapply(7:12,function(i){
  tot=dat[i,2]
  p=dat[i,3]/100
  rep(c(0,1),round(tot*c(1-p,p)))
})
allfemales<-Reduce(c,females)
plot(0,type="n",xlim=c(0,50),ylim=c(0,100),xaxt="n",yaxt="n",xlab="",ylab="")
PCH=LETTERS[rep(1:6,sapply(males,length))]
o<-order(allmales)
points(makematrix(allmales,100),col=2-allmales[o],pch=PCH[o],cex=0.6)
PCH=LETTERS[rep(1:6,sapply(females,length))]
o<-order(allfemales)
points(makematrix(allfemales,100,30),col=2-allfemales[o],pch=PCH[o],cex=0.6)
abline(v=29)
plot(0,type="n",xlim=c(0,80),ylim=c(0,130),xaxt="n",yaxt="n",xlab="",ylab="")
for(i in seq(along=males)){
  points(makematrix(males[[i]],20,0,22*(i-1)),col=2-sort(males[[i]]),pch=LETTERS[i],cex=0.6)
  points(makematrix(females[[i]],20,47,22*(i-1)),col=2-sort(females[[i]]),pch=LETTERS[i],cex=0.6)
  if(i>1) abline(h=22*(i-1)-0.5)
  }
abline(v=45)

# the effect goes away when we position by major
y=cbind(dat[1:6,3],dat[7:12,3])
matplot(1:6,y,xaxt="n",xlab="major",ylab="percent",col=c("blue","red"),cex=1.5)
legend("topright",c("Male","Female"),col=c("blue","red"),pch=c("1","2"),box.lty=0,cex=0.75)
mean(y[,1]-y[,2])
