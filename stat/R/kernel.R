"Kernel (kernel) regression."
# Generate data
n = 100
p = 10
noise.sd = 0.1
set.seed(123456)
X = matrix(runif(n*p),n,p)
mX = cos(5*pi*X[,1]) + 5*X[,2]^2
e = rnorm(n, 0, noise.sd)
Y = mX + e

# kernel regression
H=seq(0.1, 1.0, 0.01)
cvScore = krgcv(X, Y, H)
h=H[which.min(cvScore)]
print(h)
r = kr(X, Y, h, X)
risk=mean((r - mX)^2)
print(risk)

# Generalized additive model (generalized gam GAM)
require(gam)
output = gam(Y~lo(x.1)+lo(x.2)+lo(x.3)+lo(x.4)+lo(x.5)+lo(x.6)
+lo(x.7)+lo(x.8)+lo(x.9)+lo(x.10), family = gaussian,
data=data.frame(x=X, y=Y))
summary(output)
r = predict(output, newdata=data.frame(x=X))
risk = mean((r - mX)^2)
print(risk)
par(mfrow=c(2,5))
plot(output)

# SPaM (Sparsed additive model sparse)
#spam, select bandwidth and regularizer using GCV
H=seq(0.01, 0.05, 0.002) #candidate bandwidth
cvScores=rep(0, length(H))
outputs=list()
indexL=rep(0, length(H))
for(j in 1:length(H)){ #choose bandwidth
h=H[j] #current bandwidth
lambdas=seq(0, 0.4, 0.02) #candidate lambda
cvScoresEx=rep(0, length(lambdas))
outputsEx=list()
for(i in 1:length(lambdas)){
outputsEx[[i]] = spam(X, Y, h, lambdas[i], 10, 1e-3)
cvScoresEx[i] = outputsEx[[i]]$cvScore
}

    # Plot
    ## plot(lambdas, cvScoresEx, "l");
    ## record the best lambda for this bandwidth
    indexL[j]=which.min(cvScoresEx)
    cvScores[j] = cvScoresEx[indexL[j]]
    outputs[[j]] = outputsEx[[indexL[j]]]
    print(sprintf("*****H=%f", h))
}

# Retrieve best paramters
index=which.min(cvScores)
output=outputs[[index]]
print(sprintf("The optimum h=%f lambda=%f, with GCV=%f, DF=%f",
    H[index], lambdas[indexL[index]], cvScores[index], outputs[[index]]$df))
print(sprintf("%d out of %d components are selected.",sum(output$fnorm!= 0), p))
#draw the curves
ymin=min(Y) - 1
ymax=max(Y)
par(mfrow=c(2,5))
for(j in 1:p){
    plot(X[,j], Y, ylim=c(ymin, ymax), xlab="", ylab="")
    points(X[,j], output$f[,j]+mean(Y), col="red")
}
risk=mean((output$r - mX)^2)
print(risk)
