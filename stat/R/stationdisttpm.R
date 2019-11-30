# A function which will return the stationary distribution of an ergodic Markov chain
# This function returns the stationary distribution of an ergodic Markov chain.
stationdistTPM <-
function(M)  {
  eigenprob <- eigen(t(M))
  temp <- which(round(eigenprob$values,1)==1)
  stationdist <- eigenprob$vectors[,temp]
  stationdist <- stationdist/sum(stationdist)
  return(stationdist)
}
