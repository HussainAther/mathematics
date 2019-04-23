# Graph of normal probability density function, with comb of intervals.
meanval = 0.0 # mean of distribution.
sdval = 0.2 # standard deviation 
low = meanval - 3*sdval # low end of x-axis
high = meanval + 3*sdval # high end of x-axis
dx = 0.02 # interval width on x-axis

# Specify comb points along the x axis:
x = seq(from=xlow,to=xhigh,by=dx)

# Compute y values, i.e., probability density at each value of x:
 y = ( 1/(sdval*sqrt(2*pi)) ) * exp( -.5 * ((x-meanval)/sdval)ˆ2 )

# Plot the function. "plot" draws the intervals. "lines" draws the bell curve.
plot( x , y , type="h" , lwd=1 , cex.axis=1.5, xlab="x", 
    ylab="p(x)" , cex.lab=1.5, main="Normal Probability Density" , cex.main=1.5 )

# Approximate the integral as the sum of width * height for each interval.
text(-sdval , .9*max(y) , bquote( paste(mu ," = " ,.(meanval)) ) , adj=c(1,.5) )
text(-sdval , .8*max(y) , bquote( paste(sigma ," = " ,.(sdval)) ) , adj=c(1,.5) )
text(sdval , .9*max(y) , , adj=c(0,.5) ) sdval , .8*max(y) , bquote(
text(sdval , .8*max(y) , bquote(paste( sum(,x,), "", Delta, "x p(x) = ", .(signif(area, 3)))), adj=c(0,.5)) 

# Save plot
dev.copy2eps( file = "IntegralOfDensity.eps" )
