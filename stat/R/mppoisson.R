# most powerful poisson
# The most powerful test for a sample from Poisson distribution is given here. The test is obtained by an application of the Neyman-Pearson lemma. 
MPPoisson <-
function(Hlambda, Klambda, alpha,n)  {
  Hlambda <- n*Hlambda
  Klambda <- n*Klambda
  nn <- n*Hlambda 
  if(Hlambda<Klambda)  {
    k <- min(which((1-ppois(0:nn,lambda=Hlambda))<alpha))-1
    gamma <- (alpha-1+ppois(k,lambda=Hlambda))/dpois(k,lambda=Hlambda)
    return(list=c(k,gamma))
  }
  else {
    k <- max(which((ppois(0:nn,lambda=Hlambda))<alpha))
    gamma <- (alpha-ppois(k-1,lambda=Hlambda))/dpois(k,lambda=Hlambda)
    return(list=c(k,gamma))
  }
}
