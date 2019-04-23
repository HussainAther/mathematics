"Introduce independent and identically distributed Gausisan noise with mean 0 and
standard deviation .15 to two different curves."
x = runif(300,0,3)
yr = true.r(x)+rnorm(length(x),0,0.15)
ys = true.s(x)+rnorm(length(x),0,0.15)
par(mfcol=c(2,1))
plot(x,yr,xlab="x",ylab=expression(r(x)+epsilon))
curve(true.r(x),col="grey",add=TRUE)
plot(x,ys,xlab="x",ylab=expression(s(x)+eta))
curve(true.s(x),col="grey",add=TRUE)
"Use both smoothing and and function roughness. Estime regression function at x = 1.6 
by averaging observations in which 1.5 < x < 1.7. The average location is shown
by the large black diamond."
par(mfcol=c(2,1))
x.focus <- 1.6; x.lo <- x.focus-0.1; x.hi <- x.focus+0.1
colors=ifelse((x<x.hi)&(x>x.lo),"black","grey")
plot(x,yr,xlab="x",ylab=expression(r(x)+epsilon),col=colors)
curve(true.r(x),col="grey",add=TRUE)
points(x.focus,mean(yr[(x<x.hi)&(x>x.lo)]),pch=18,cex=2)
plot(x,ys,xlab="x",ylab=expression(s(x)+eta),col=colors)
curve(true.s(x),col="grey",add=TRUE)
points(x.focus,mean(ys[(x<x.hi)&(x>x.lo)]),pch=18,cex=2)
par(mfcol=c(1,1))
