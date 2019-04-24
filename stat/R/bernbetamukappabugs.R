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

