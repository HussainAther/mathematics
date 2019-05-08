"For a single scalar field on a plane, we take a function of mu(x) = 0 and gamma(x, x') = exp(-||x-x'||) so
we're using units that have variance 1 and correlation length 1. We want to predict the value of the field at
the origin. We have observations on a square grid in which the grid spacing is 1. We have alpha = 0 and, to find
beta, we evaluate exp(-||x-x'||) for each pair of points."
coords <- expand.grid(x = c(-1, 0, 1), y = c(-1, 0, 1))
predict.pt <- which(coords$x == 0 & coords$y == 0)
distances <- dist(coords)
distances <- as.matrix(distances)
covars <- exp(-distances)
Cov.YZ <- covars[predict.pt, -predict.pt]
Var.Z <- covars[-predict.pt, -predict.pt]
beta <- solve(Var.Z) %*% Cov.YZ
signif(data.frame(coords[-predict.pt, ], coef = beta), 3)
