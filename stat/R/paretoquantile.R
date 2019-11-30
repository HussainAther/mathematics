# Quantile of Pareto RV
# A simple function is given here which returns the quantiles for a Pareto RV. 
pareto_quantile <-
function(p,scale,shape) scale/(1-p)^{1/shape}
