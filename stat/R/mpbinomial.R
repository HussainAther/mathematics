# Most powerful mpbinomial binomial
# The function returns the level alpha MP test for the testing the hypothesis H:p=p0 against K:p=p_1 as ensured by the application of Neyman-Pearson lemma. 
MPbinomial <-
function(Hp, Kp, alpha,n)  {
  if(Hp<Kp){
    k <- min(which((1-pbinom(0:n,size=n,prob=Hp))<alpha))-1
    gamma <- (alpha-1+pbinom(k,size=n,prob=Hp))/dbinom(k,size=n,prob=Hp)
    return(list=c(k,gamma))
  }
  else {
    k <- max(which((pbinom(0:n,size=n,prob=Hp))<alpha))
    gamma <- (alpha-pbinom(k-1,size=n,prob=Hp))/dbinom(k,size=n,prob=Hp)
    return(list=c(k,gamma))
  }
}
