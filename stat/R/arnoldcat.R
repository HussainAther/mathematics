"Arnold's (Arnold arnold) cat map. In mathematics, Arnold's cat map is a 
chaotic map from the torus into itself, named after Vladimir Arnold, who 
demonstrated its effects in the 1960s using an image of a cat, hence the name."
arnold.map <- function(v) {
  theta <- v[1]
  phi <- v[2]
  theta.new <- (theta+phi)%%1
  phi.new <- (theta+2*phi)%%1
  return(c(theta.new,phi.new))
}
rarnold <- function(n,seed) {
  z <- vector(length=n)
  for (i in 1:n) {
    seed <- arnold.map(seed)
    z[i] <- seed[1]
  }
return(z) }
