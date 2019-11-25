# Spatial smoothing with splines
coords <- expand.grid(x = c(-1, 0, 1), y = c(-1, 0, 1))
predict.pt <- which(coords$x == 0 & coords$y == 0)
distances <- dist(coords)
distances <- as.matrix(distances)
covars <- exp(-distances)
Cov.YZ <- covars[predict.pt, -predict.pt]
Var.Z <- covars[-predict.pt, -predict.pt]
beta <- solve(Var.Z) %*% Cov.YZ
signif(data.frame(coords[-predict.pt, ], coef = beta), 3)
plot(coords, xlab = "longitude", ylab = "latitude", type = "n")
points(coords[predict.pt, ], col = "red")
points(coords[-predict.pt, ], cex = 10 * sqrt(beta))
