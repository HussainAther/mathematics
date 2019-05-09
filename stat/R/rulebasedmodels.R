"Rule-based models. Build single classification trees. Use predictors for the data
to model classes for groupes categories."
library(rpart)
cartModel <- rpart(factorForm, data = training[pre2008,])
rpart(Class ~ NumCI + Weekday, data = training[pre2008,])
