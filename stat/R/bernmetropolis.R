"Apply the Metropolis (Metropolis-Hastings metropolis hastings) algorithm to estimate
a binomial proportion."
# Specify the data, to be used in the likelihood function.
# This is a vector with one component per flip,
# in which 1 means a "head" and 0 means a "tail".
myData=c(1,1,1,1,1,1,1,1,1,1,1,0,0,0)

# Define the Bernoulli likelihood function, p(D|theta).
# The argument theta could be a vector, not just a scalar.
likelihood = function( theta , data ) {
    z=sum(data==1)
    N = length(data)
    pDataGivenTheta = theta^z * (1-theta)^(N-z)
    # The theta values passed into this function are generated at random,
    # and therefore might be inadvertently greater than 1 or less than 0.
    # The likelihood for theta > 1 or for theta < 0 is zero: 
    pDataGivenTheta[theta > 1 | theta < 0] = 0
    return(pDataGivenTheta)
}

# Define the prior density function. For purposes of computing p(D),
# at the end of this program, we want this prior to be a proper density. 
# The argument theta could be a vector, not just a scalar.
prior = function(theta) {
    prior = rep(1, length(theta)) # uniform density over [0,1]
    # For kicks, here’s a bimodal prior. To try it, uncomment the next line.
    #prior = dbeta(pmin(2*theta, 2*(1-theta)), 2, 2)
    # The theta values passed into this function are generated at random,
    # and therefore might be inadvertently greater than 1 or less than 0.
    # The prior for theta > 1 or for theta < 0 is zero:
    prior[theta>1|theta<0]=0
    return(prior)
}

# Define the relative probability of the target distribution,
# as a function of vector theta. This target distribution is the 
# unnormalized posterior distribution.
targetRelProb = function(theta, data) {
    targetRelProb = likelihood(theta, data) * prior(theta)
    return(targetRelProb)
}

# Specify the length of the trajectory, i.e., the number of jumps to try.
trajLength = 11112 # arbitrary large number

# Initialize the vector that will store the results.
trajectory = rep(0, trajLength)

# Specify where to start the trajectory.
trajectory[1] = 0.50 # arbitrary value

# Specify the burn-in period.
burnIn = ceiling( .1 * trajLength ) # arbitrary number, less than trajLength

# Initialize accepted, rejected counters, just to monitor performance.
nAccepted = 0
nRejected = 0 

# Specify seed to reproduce same random walk
set.seed(12345)

# Generate the random walk. The "t" index is time or trial.
for (t in 1:(trajLength-1)) {
    currentPosition = trajectory[t]
    # Use the proposal distribution to generate proposed jump.
    # The shape and variacne of the proposal distribution can be changed
    # to whatever you think is appropriate for the target distribution.
    proposedJump = rnorm(1, mean=0, sd = .1)
    # Compute the probability of accepting the proposed jump.
    probAccept = min(1, targetRelProb(currentPosition + proposedJump, myData)
                        / targetRelProb(currentPosition, myData))
    # Generate a random uniform value from the interval [0, 1] to
    # decide whether or not to accept the proposed jump.
    if (runif(1) < probAccept) {
        # accept the proposed jump
        trajectory[t+1] = currentPosition + proposedJump
        # increment the accepted counter
        if (t > burnIn) { nAccepted = nAccepted + 1}
        } else {
            # reject the proposed jump, stay at current position
            trajectory[t+1] = currentPosition
            # increment the rejected counter
            if (t > burnIn) {nRejected = nRejected + 1}
    }
}

# Extract the post-burnIn portion of the trajectory
acceptedTraj = trajectory[(burnIn+1) : length(trajectory)]

# Display the posterior
source("plotPost.R")
histInfo = plotPost(acceptedTraj, xlim=c(0, 1), breaks=30)

# Display the rejected/accepted ratio in the plot
# Get the highest point and mean of the plot for text
densMax = max(histInfo$density)
meanTraj = mean(acceptedTraj)
sdTraj = sd(acceptedTraj)
if (meanTraj > .5) {
    xpos = 0
    xadj = 0
    } else {
    xpos = 1
    xadj = 1
    }
    text(xpos, .75*densMax, bquote(N[pro] * "=" * .(length(acceptedTraj)) * " " *
        frac(N[acc],N[pro]) * "=" * .(signif( nAccepted/length(acceptedTraj) , 3 ))) , adj=c(xadj,0))
}

