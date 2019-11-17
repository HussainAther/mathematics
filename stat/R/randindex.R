"Rand index calculation."
randindex <- function(clustering, classes)
{ 
  mean(outer(1:length(clustering), 1:length(classes),
             function(i, j)
             ifelse(i!=j,
                    clustering[i]==clustering[j] & classes[i]==classes[j]  |
                    clustering[i]!=clustering[j] & classes[i]!=classes[j, NA)),
       na.rm=TRUE)
}
