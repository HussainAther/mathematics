# Highest (posterior) density interval (highest Posterior) (HDI hdi) of the 
# inverse cumulative density function (icdf ICDF) for the corresponding
# probability distribution.

HDIofICDF = function(ICDFname, credMass=0.95, tol=1e-8, ...) {
    # ICDFname is the inverse cumulative density function of the distribution.
    # credMass is the desired mass of the HDI region.
    # tol is the tolerance to optimize the function.
    # Return the highest density interval (HDI) limmits in a vector.
    incredMass = 1.0 - credMass # inverse of the input
    intervalWidth = function(lowTailPr, ICDFname, credMass, ...) {
        ICDFname(credMass + lowTailPr, ...) - ICDFname(lowTailPr, ...)
    } 
