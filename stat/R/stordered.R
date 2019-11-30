# Simulating Random Observations from an Arbitrary Distribution
# An implementation of the algorithm for simulation of observations from an arbitrary discrete distribution is provided here. 
ST_Ordered <-
function(N,x,p_x){
  x <- x[order(p_x,decreasing=TRUE)]
  F_x <- cumsum(sort(p_x,decreasing=TRUE))
  disc_sim <- numeric(length=N)
  for(i in 1:N){
    temp <- runif(1)
    disc_sim[i] <- x[min(which(F_x>temp))]
  }
  return(disc_sim)
}
