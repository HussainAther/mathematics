"When smoothing one dimensional data, we want to find an approximation to the true conditional
expectation or reegression function μ. We were controlling how smooth we make indirectly through
the bandwith of the kernels, but we can use a more direct method of controlling smoothness itself by
minimizing the spline objective function."
require(pdfetch)
sp <- pdfetch_YAHOO("SPY", fields = "adjclose", from = as.Date("1993-02-09"),
    to = as.Date("2015-02-09"))
