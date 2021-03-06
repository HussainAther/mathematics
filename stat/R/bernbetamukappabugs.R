"Rosa, Rosa, Sarner, and Barrett (1998) investigated therapeutic touch (TT) among medical practitioners."
"TT is is a technique in which nurses sweep their hands 5–10 cm over a patient’s body and (claim to) sense "
"depleted or congested areas of the patient’s “energy field”. The TT practitioners then sweep their hands to"
"re-pattern and smooth the energy field, resulting in healing of the patient. TT has had a notable range of"
"proponents, including some professional organizations."

"These data are precisely of the form that can be modeled by Figure 9.7. Each prac- titioner corresponds to "
"a “coin” being flipped 10 times, and the underlying ability of the jth practitioner is denoted θj. "
"The practitioners are assumed to be randomly representa- tive of the group of all practitioners, and the "
"group has a mean ability denoted by μ. The dependency of the individual abilities on the group mean is measured by κ."

graphics.off()
rm(list=ls(all=TRUE))
library(BRugs)

# Model using BUGS
modelString = "model {
    # Likelihood:
    for ( t in 1:nTrialTotal ) {
        y[t]  ̃ dbern( theta[ coin[ t ] ] )
    }
    # Prior:
    for ( j in 1:nCoins ) {
        theta[j]  ̃ dbeta( a , b )I(0.0001,0.9999)
    }
    a <- mu * kappa
    b <- (1.0 - mu) * kappa
    mu - dbeta(Amu, Bmu)
    kappa - dgamma(Skappa, Rkappa)
    Amu <- 2.0
    Bmu <- 2.0
    Skappa <- pow(10, 2)/pow(10,2)
}
"

# Write the modelString to a file, using R commands.
.temp = file("model.txt","w"); writeLines(modelString,con=.temp); close(.temp)

# Check the model
modelCheck( "model.txt" )

# Therapeutic touch data
z = c(1,2,3,3,3,3,3,3,3,3,4,4,4,4,4,5,5,5,5,5,5,5,6,6,7,7,7,8)
N = rep(10,length(z))
coin=NULL;y=NULL

for (coinIdx in 1:length(N)) {
coin = c(coin, rep(coinIdx,N[coinIdx]))
    y = c(y, rep(1,z[coinIdx]), rep(0,N[coinIdx]-z[coinIdx]))
}

nTrialTotal = length(y)
    nCoins = length( unique(coin)
    dataList = list(
        y=y,
    coin = coin ,
    nTrialTotal = nTrialTotal ,
    nCoins = nCoins
)

# Initialize chains
nChains = 3
modelCompile( numChains = nChains ) # BRugs tells BUGS to compile the model.
modelGenInits() # BRugs tells BUGS to randomly initialize the chains.


# Run some initial steps without recording them, to burn-in the chains:
burninSteps = 1000
modelUpdate(burninSteps)

# BRugs tells BUGS to keep a record of the sampled values:
samplesSet(c("mu" , "kappa" , "theta"))
nPerChain = 1000
modelUpdate(nPerChain, thin=10)

# Check for mixing and autocorrelation:
source("plotChains.R")
plotChains( "mu" , saveplots=F )
plotChains( "kappa" , saveplots=F )
plotChains( "theta[1]" , saveplots=F )

# Extract the posterior sample from BUGS:
muSample = samplesSample("mu") # BRugs gets sample from BUGS
kappaSample = samplesSample("kappa") # BRugs gets sample from BUGS
thetaSample = matrix(0, nrow=nCoins, ncol=nChains*nPerChain)
for (coinIdx in 1:nCoins) {
    nodeName = paste( "theta[" , coinIdx , "]" , sep="")
    thetaSample[coinIdx,] = samplesSample(nodeName)
}

# Make a graph using R commands:
source("plotPost.R")
if(nCoins<=5){
windows(3.2*3,2.5*(1+nCoins))
layout( matrix( 1:(3*(nCoins+1))
par(mar=c(2.95,2.95,1.0,0),mgp=c(1.35,0.35,0),oma=c( 0.1, 0.1, 0.1, 0.1))
nPtsToPlot = 500
plotIdx = floor(seq(1,length(muSample),length=nPtsToPlot))
kPltLim = signif( quantile( kappaSample , p=c(.01,.99) ) , 4 )
plot(muSample[plotIdx], kappaSample[plotIdx], type="p", ylim=kPltLim,
    xlim=c(0,1), xlab=expression(mu), ylab=expression(kappa), cex.lab=1.5)
plotPost(muSample, xlab="mu", xlim=c(0,1), main="", breaks=20)
plotPost(kappaSample , xlab="kappa", main="", breaks=20, HDItextPlace=.6)
for (coinIdx in 1:nCoins) {
    plotPost(thetaSample[coinIdx,], xlab=paste("theta",coinIdx,sep=""),
        xlim=c(0,1), main="", breaks=20, HDItextPlace=.3)
    plot(thetaSample[coinIdx,plotIdx], muSample[plotIdx], type="p",
        xlim=c(0,1), ylim=c(0,1), cex.lab=1.5,
        xlab=bquote(theta[.(coinIdx)]), ylab=expression(mu))
    plot(thetaSample[coinIdx,plotIdx], kappaSample[plotIdx], type="p",
        xlim=c(0,1), ylim=kPltLim, cex.lab=1.5,
        xlab=bquote(theta[.(coinIdx)]), ylab=expression(kappa))
    }
    dev.copy2eps(file=paste("BernBetaMuKappaBugs",paste(z,collapse=""),".eps",sep=""))
}
