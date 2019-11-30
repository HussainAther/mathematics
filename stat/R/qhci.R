"Confidence Interval -Quesenberry And Hurst"
"confidence interval quesenberry hurst"
# Quesenberry-Hurst Simultaneous Confidence Interval
# Quesenberry and Hurst (1964) have obtained the "simultaneous confidence intervals" for the vector of success in a multinomial distribution. 
QH_CI <-
function(x,alpha)  {
  k <- length(x); n <- sum(x)
  QH_lcl <- (1/(2*(sum(x)+qchisq(1-alpha/k,k-1))))*{qchisq(1-alpha/k,k-1)+2*x-sqrt( qchisq(1-alpha/k,k-1)*(qchisq(1-alpha/k,k-1)+ 4*x*(sum(x)-x)/sum(x))) }
  QH_ucl <- (1/(2*(sum(x)+qchisq(1-alpha/k,k-1))))*{qchisq(1-alpha/k,k-1)+2*x+sqrt( qchisq(1-alpha/k,k-1)*(qchisq(1-alpha/k,k-1)+ 4*x*(sum(x)-x)/sum(x))) }  
  return(cbind(QH_lcl,QH_ucl))
}
