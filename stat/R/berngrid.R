"Grid approximation to infer binomial proportion."
BernGrid = function(Theta, pTheta, Data, credib=.95, nToPlot=length(Theta)) {
    # Bayesian updating for Bernoulli likelihood and prior specified on a grid.
    # Theta is a vector of theta values between 0 and 1.
    # pTheta is a vector of corresponding probability masses.
    # Data is a vector of 1s and 0s (corresponding to a and b, respectively).
    # credib is the probability of mass of the credible interval, default is .95.
    # nToPlot is the number of grid points to plot. default is all.
    # Return pThetaGivenData, vector of posterior probability masses over Theta.
    # Create a three-panel graph of prior, likelihood, and posterior probability
    # masses with credible interval.

    # Create summary values of Data
    z = sum(Data==1) # number of 1's in Data
    N = length( Data ) # number of flips in Data

    # Compute the likelihood of the Data for each value of Theta.
    pDataGivenTheta = Theta^z * (1-Theta)^(N-z)
    
    # Compute the evidence and the posterior.
    pData = sum(pDataGivenTheta * pTheta) 
    pThetaGivenData = pDataGivenTheta * pTheta / pData
     
    # Plot the results.
    layout(matrix(c(1, 2, 3), nrow=3, ncol=1, byrow=FALSE)) # 3x1 panels
