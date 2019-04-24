# Specify the grid on theta1,theta2 parameter space.
nInt = 501 # arbitrary number of intervals for grid on theta.
theta1 = seq(from=((1/nInt)/2), to=(1-((1/nInt)/2)), by=(1/nInt))
theta2 = theta1

# Specify the prior probability _masses_ on the grid.
priorName = c("Beta","Ripples","Null","Alt")[1]
if (priorName == "Beta") {
    a1=3; b1=3; a2=3; b2=3
    prior1 = dbeta(theta1, a1, b1)
    prior2 = dbeta(theta2, a2, b2)
    prior = outer(prior1, prior2) # density
    prior = prior / sum( prior ) # convert to normalized mass
}
if ( priorName == "Ripples" ) {
    rippleAtPoint = function( theta1 , theta2 ) {m1 = 0 ; m2 = 1 ; k = 0.75*pi
    sin((k*(theta1-m1))^2 + (k*(theta2-m2))^2)^2} prior = outer( theta1 , theta2 , rippleAtPoint )
    prior = prior / sum(prior) # convert to normalized mass
}
if (priorName == "Null") {  # 1’s at theta1=theta2, 0’s everywhere else.
    prior = diag(1 , nrow=length(theta1) , ncol=length(theta1))
    prior = prior / sum(prior) # convert to normalized mass
}
if (priorName == "Alt") {
    # Uniform:
    prior = matrix( 1 , nrow=length(theta1) , ncol=length(theta2) )
    prior = prior / sum( prior ) # convert to normalized mass
}
