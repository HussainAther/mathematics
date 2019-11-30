# Trimean is a measure of location and is the weighted average of the median and two other quartiles. 
TM <- function(x) {
   qs <- quantile(x,c(0.25,0.5,0.75))
   return(as.numeric((qs[2]+(qs[1]+qs[3])/2)/2))
}
