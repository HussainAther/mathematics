"Newton's (newton Newton) method of optimization minimizes a quadratic approximation to the 
function we're interested in. The true minimum is a fixed point of the equation

θ(n+1) = θ(n) − f ′(θ(n)) / f ′′(θ(n))."

my.newton = function(f, f.prime, f.prime2, beta0, tolerance=1e-3, max.iter=50) {
  beta = beta0
  old.f = f(beta)
  iterations = 0
  made.changes = TRUE
  while(made.changes & (iterations < max.iter)) {
   iterations <- iterations +1
   made.changes <- FALSE
   new.beta = beta - f.prime(beta)/f.prime2(beta)
   new.f = f(new.beta)
   relative.change = abs(new.f - old.f)/old.f -1
   made.changes = (relative.changes > tolerance)
   beta = new.beta
   old.f = new.f
}
if (made.changes) {
  warning("Newton's method terminated before convergence") }
return(list(minimum=beta, value=f(beta), deriv=f.prime(beta),
    deriv2=f.prime2(beta), iterations=iterations,
    converged=!made.changes))
}
