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
