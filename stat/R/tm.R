# Trimmed Mean
# The trimean can be viewed as the average of median and average of the lower and upper quartiles.
TM <-
function(x) {
  qs <- quantile(x,c(0.25,0.5,0.75))
  return(as.numeric((qs[2]+(qs[1]+qs[3])/2)/2))
}
