"Rand index calculation."
randindex <- function(clustering, classes)
{ 
  mean(outer(1:length(clustering), 1:length(classes),

