"Kernel (kernel) regression."
"Generate n = 100 observations from the model
Yi = m(Xi) + ei 

where ei iid∼ N(0, σ2), σ = 0.1,

Xi ∼ U([0, 1]10) and m(x) = cos(5πxi) + 5x_2**2

Note that x is 10-dimensional but m(x) only depends on x1 and x2. Estimate m using (i) multivariate
kernel regression, (ii) an additive model, (iii) a sparse additive model. Be sure to include code and
choose tuning parameters correctly. For each estimator, report."

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

ksm = function(x, h, t = x){
    #generate kernel smooth matrix
    if(!is.matrix(x)) x = as.matrix(x)
    if(!is.matrix(t)) t = as.matrix(t)
    n = nrow(x)
    d = ncol(x)
    nt = nrow(t)
    K = matrix(NA, n, nt)
    for(i in 1:nt){
        diff = matrix(t[i,], n, d, byrow = TRUE) - x
        K[,i] = dnorm(sqrt(rowSums(diff^2)), 0, h)
    }
    return(K)
}

normalizeKM = function(K){
    #normalize columns of K, sum to 1
    l = apply(K, 2, function(x) x/sum(x))
    return(l)
}

krgcv = function(x, y, hs){
    #kernel regression GCV score
    nh=length(hs)
    cvScore=rep(0, nh)
    for(i in 1:nh){
        K = ksm(x, hs[i], x)
        l = normalizeKM(K)
        r = t(l) %*% y
        W = dnorm(0, 0, hs[i])/colSums(K)
        cvScore[i] = sum(((r - y)/(1 - W))^2)
    }
    return(cvScore)
}

kr = function(x, y, h, t){
    #kernel regression
    K = ksm(x, h, t)
    l = normalizeKM(K)
    r = t(l) %*% y
    return(r)
}

tr = function(m){
    #matrix trace
    if(nrow(m) != ncol(m)) print("Error in tr(). matrix not square")
    return(sum(diag(m)))
}

# Sparse additive model (SpAM sparse)
spam = function(x, y, h, lambda, maxIter=20, epsilon=1e-3){
    n = nrow(x)
    p = ncol(x)
    fs=matrix(0, n, p) # components
    Ss=list() # smooth matrices
    ## print("generating smoothing matrices...")
    for(j in 1:p) Ss[[j]] = t(normalizeKM(ksm(x[,j], h, x[,j])))
    ## print("complete.")
    ## center the response
    alpha = mean(y)
    y = y - alpha
    oldErr = 1e30
    newfs = fs
    for(iter in 1:maxIter){
        for(j in 1:p){
            Rj = y - rowSums(newfs[,-j])
	    Pj = Ss[[j]] %*% Rj
	    sj = sqrt(mean(Pj^2))
            fj = max(0, 1 - lambda/sj) * Pj
            newfs[,j] = fj - mean(fj)
         }

         ## calculate the residual
         r = rowSums(newfs)
         residual = r - y
         mse = mean(residual^2)
         print(sprintf("Iteration %d: Residual=%f", iter, mse))
         ## test termination
         if(mse < epsilon || oldErr - mse < epsilon){
             break
         }else{
             oldErr = mse
             fs = newfs
         }
    } 
    r = rowSums(fs) + alpha #regression result
    fnorm = sqrt(colSums(fs^2)) #norm of components
    df=0 #degree of freedom
    for(j in 1:p) if(fnorm[j] > 0) df = df + tr(Ss[[j]])
    #GCV score
    cvScore = mean((y + alpha - r)^2)/max(0, 1 - df/n)^2
    return(list(f=fs, fnorm=fnorm, S=Ss, r=r, df=df, cvScore=cvScore, alpha=alpha))
} 
