# Simulation for Poisson Distribution
# A simple function to understand the algorithm to simulate (psuedo-)observations from binomial distribution. This function is not an alternative to the "rpois" function.
Poisson_Sim <-
function(lambda,n)  {
  x = numeric(n)
  for(i in 1:n){
    j = 0; p = exp(-lambda); F = p
    temp = runif(1)
    while((F>temp)==FALSE){
      p = lambda*p/(j+1); F = F+p; j=j+1
    }
    x[i] = j
  }
  return(x)
}
