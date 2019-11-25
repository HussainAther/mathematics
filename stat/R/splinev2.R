# Spatial smoothing with splines
coords <- expand.grid(x = c(-1, 0, 1), y = c(-1, 0, 1))
predict.pt <- which(coords$x == 0 & coords$y == 0)
distances <- dist(coords)
distances <- as.matrix(distances)
