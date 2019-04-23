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
