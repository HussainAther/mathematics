library(knitr)
opts_chunk$set(fig.path=paste0("figure/", sub("(.*).Rmd","\\1",basename(knitr:::knit_concord$get('infile'))), "-"))

# Collinearity - look for this in the design matrix to determine
# if the model fits.
