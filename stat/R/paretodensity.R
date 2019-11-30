# Pareto distribution density
# A simple function is given here which returns the density function values for a Pareto RV. A more efficient implementation is obtainable in the function "dpareto" from the "VGAM" package. 
pareto_density <-
function(x,scale,shape) {
  lpd <- ifelse(x<scale, -Inf, log(shape) + shape*log(scale) - (shape+1)*log(x))
  return(exp(lpd))
}
