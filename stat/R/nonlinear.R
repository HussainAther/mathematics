"Nonlinear (nonlinear) classification models."
library(mda)
mdaModel <- mda(Class ~ ., data = training[pre2008, c("Class", reducedSet)],
                subclasses = 3)
