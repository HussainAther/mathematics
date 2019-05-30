"Adaboost Model classification is a boosting algorithm that improves on classifiers by
increasing their weights and getting their votes to create the final combined model."
install.packages("adabag")
library(adabag)

"Load data."
set.seed(123)
a <- sample(1:10, 250, replace = T)
b <- sample(10:20, 250, replace = T)
flag <- ifelse(a > 5 & b > 10, "red", ifelse(a<3,"yellow", "green"))
df <- data.frame(a = a, b = b, flag = as.factor(flag))

"Create and train test data."
train <- df[1:200,]
test <- df[200:250,]

"Build model."
model_adabag <- boosting(flag~a+b, data=train, boos=TRUE, mfinal=10)
names(model_adabag)
