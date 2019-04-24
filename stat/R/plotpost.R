"Plot a histogram of a sample, with various useful annotations. You need to source it in R before calling it, of course. Here are the annotations that the program can add to the histogram"
plotPost = function(paramSampleVec, credMass=0.95, compVal=NULL,
    HDItextPlace=0.7, ROPE=NULL, yaxt=NULL, ylab=NULL,
    xlab=NULL, cex.lab=NULL, cex=NULL, xlim=NULL, main=NULL,
    showMode=F, ... ) {

    # Override defaults of hist function, if not specified by user:
    # (additional arguments "..." are passed to the hist function)
    if (is.null(xlab)) xlab="Parameter"
    if (is.null(cex.lab)) cex.lab=1.5
    if (is.null(cex)) cex=1.4
    if (is.null(xlim)) xlim=range( c( compVal , paramSampleVec ) ) if ( is.null(main) ) main=""
    if (is.null(yaxt)) yaxt="n"
    if (is.null(ylab)) ylab=""

    # Plot histogram.
    par(xpd=NA)

    histinfo = hist(paramSampleVec, xlab=xlab, yaxt=yaxt, ylab=ylab, freq=F,
        col="lightgrey", border="white", xlim=xlim, main=main, cex=cex, cex.lab=cex.lab, ...)

    # Display mean or mode.
    if (showMode==F){
        meanParam = mean( paramSampleVec )
        text(meanParam, .9*max(histinfo$density), bquote(mean==.(signif(meanParam,3))),
            adj=c(.5,0), cex=cex)
    } else {
        dres = density(paramSampleVec)
        text(meanParam, .9*max(histinfo$density), bquote(mode==.(signif(modeParam,3))),adj=c(.5,0) , cex=cex))
    }

    # Display the comparison value.
    if (!is.null(compVal)) {
        pcgtCompVal = round(100 * sum(paramSampleVec > compVal) / length(paramSampleVec), 1)
        pcltCompVal = 100 - pcgtCompVal
        lines(c(compVal,compVal), c(.5*max(histinfo$density), 0), lty="dashed", lwd=2)
        text(compVal, .5*max(histinfo$density), bquote(.(pcltCompVal)*"% <= " *
            .(signif(compVal,3)) * " < "*.(pcgtCompVal)*"%" ), adj=c(pcltCompVal/100,-0.2), cex=cex)
        }
    
        # Display the ROPE
        if (!is.null(ROPE)) {
            pcInROPE = (sum(paramSampleVec > ROPE[1] & paramSampleVec < ROPE[2]) / length(paramSampleVec))
            ROPEtextHt = .35*max(histinfo$density)
            lines(c(ROPE[1], ROPE[1]), c(ROPEtextHt,0), lty="dotted", lwd=2)
            lines(c(ROPE[2], ROPE[2]), c(ROPEtextHt,0), lty="dotted", lwd=2)
            text(mean(ROPE), ROPEtextHt, bquote(.(round(100*pcInROPE))*"% in ROPE"), adj=c(.5,-0.2), cex=1)
        }
        # Display the HDI.
        source("HDIofMCMC.R")
        HDI = HDIofMCMC(paramSampleVec, credMass)
        lines(HDI, c(0,0), lwd=4)
        text(mean(HDI), 0, bquote(.(100*credMass) * "% HDI" ), adj=c(.5,-1.9), cex=cex)
        text(HDI[1], 0 , bquote(.(signif(HDI[1],3))), adj=c(HDItextPlace,-0.5), cex=cex)
        text(HDI[2], 0 , bquote(.(signif(HDI[2],3))),
            adj=c(1.0-HDItextPlace,-0.5) , cex=cex)
        par(xpd=F)
        return(histinfo)
}
