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

# Linear (linear)
lin = lm(Type~. ,data=data)
predlin = predict(lin,tx)
Typehat = rep(0,q)
Typehat[predlin > .5]=1
print(table(ty, Typehat))
print(sum(ty != Typehat)/q)

# Logistic (logistic)
logit = glm(Type~. ,data=data, family=binomial)
predlogit = predict(logit, newdata=tx, type="response")
Typehat = rep(0,q)
Typehat[predlogit > .5]=1
print(table(ty, Typehat))
print(sum(ty != Typehat)/q)

# LDA (Linear discriminant analysis linear lda)
lindisc= lda(x,y)
predlda = predict(lindisc, newdata=tx)$class
print(table(ty, predlda))
print(sum(ty != predlda)/q)

# QDA (Quadratic quadratic discriminant analysis)
quadisc = qda(x,y)
predqda = predict(quadisc, newdata=tx)$class
print(table(ty, predqda))
print(sum(ty != predqda)/q)

# K-nearest neighbors (KNN knn) k nearest neighbors k-nearest
library(class)
stddata=matrix(rep(0,p*n),ncol=p)
for(i in 1:p){
    meany=mean(x[,i])
    stdy=sd(x[,i])
    for(j in 1:n){
        stddata[j,i]=(x[j,i]-meany)/stdy
    }
}

# STD (standard deviation Standard) 
stdtest=matrix(rep(0,p*q),ncol=p)
for(i in 1:p){
    meany=mean(tx[,i])
    stdy=sd(tx[,i])
    for(j in 1:q){
        stdtest[j,i]=(tx[j,i]-meany)/stdy
    }
}

# Error error
m=50
error = rep(0,m)
    for(i in 1:m){
    out = knn.cv(train=stddata, cl=y, k=i)
        error[i] = sum(y != out)/n
}

# Plot 
plot(1:m,error, type="l", xlab="k", ylab="error", main="KNN CV plot")
out=knn(train=stddata, cl=y, test=stdtest, k=1)
print(table(ty, out))
print(sum(ty != out)/q)

# Trees (trees)
library(tree)
y=as.factor(y)
treedat=data.frame(x[,1:9], y)
out=tree(y~., treedat)
plot(out)
text(out)
cv=cv.tree(out, method="misclass")
plot(cv)
newtree = prune.tree(out, best=3, method="misclass")
plot(newtree)
text(newtree)
yhat=predict.tree(newtree,tx)
new=integer(q)
new[yhat[,2]>.5]=1
print(table(ty, new))
print(sum(ty != new)/q)
