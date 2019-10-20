x1.points <- seq(-3,3,length.out=100)
x2.points <- x1.points
x12grid <- expand.grid(x1=x1.points,x2=x2.points)
y <- matrix(0, nrow=100, ncol=100)
y <- outer(x1.points, x2.points, f)
library(lattice)
wireframe(y~x12grid$x1*x12grid$x2,scales=list(arrows=FALSE),
  xlab=expression(x^1),ylab=expression(x^2),zlab="y")

