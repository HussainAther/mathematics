"Glass fragment data.
The goal is to predict the variable type from the others. Note that 
type takes 6 different values. First combine the first three classes 
(different types of window glass) and the last three classes so that type
now only has two values. Classify the data (window or not window) 
using (i) linear regression, (ii) logistic regression, and (iii) lda 
(using the function lda()). Compare the results."
library(MASS)
data(fgl)

# Combine first three classes 
attach(fgl)
X=fgl[,1:9]
Type=rep(0, 214)
Type[1:163]=1
data1=cbind(X,Type)
k=nrow(X)
testa=rbinom(k,1, .25)
data=data1[testa==0,]
test=data1[testa==1,]
x=data[,1:9]
tx=test[,1:9]
ty=test[,10]
y=data[,10]
n=nrow(data)
p=ncol(X)
q=nrow(tx)

# Linear
lin = lm(Type~. ,data=data)
predlin = predict(lin,tx)
Typehat = rep(0,q)
Typehat[predlin > .5]=1
print(table(ty, Typehat))
print(sum(ty != Typehat)/q)
