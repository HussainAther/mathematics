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
