"Cross-validation for univariate kernel regression. The colnames trick: component names have to be character strings; other data types will be coerced into characters when we assign them to be names. 
Later, when we want to refer to a bandwidth column by its name, we wrap the name in another coercing function, such as paste. — The vector of default bandwidths is only for illustration; 
it should not be used blindly on data, or in homework."
cv_bws_npreg <- function(x,y,bandwidths=(1:50)/50,nfolds=10) {
  require(np)
  n <- length(x)
  stopifnot(n > 1, length(y) == n)
  stopifnot(length(bandwidths) > 1)
  stopifnot(nfolds > 0, nfolds==trunc(nfolds))
  fold_MSEs <- matrix(0,nrow=nfolds,ncol=length(bandwidths))
  colnames(fold_MSEs) = bandwidths
  case.folds <- sample(rep(1:nfolds,length.out=n))
  for (fold in 1:nfolds) {
    train.rows = which(case.folds!=fold)
    x.train = x[train.rows]
    y.train = y[train.rows]
    x.test = x[-train.rows]
    y.test = y[-train.rows]
    for (bw in bandwidths) {
      fit <- npreg(txdat=x.train,tydat=y.train,
                   exdat=x.test,eydat=y.test,bws=bw)
      fold_MSEs[fold,paste(bw)] <- fit$MSE
    }
  }
  CV_MSEs = colMeans(fold_MSEs)
  best.bw = bandwidths[which.min(CV_MSEs)]
  return(list(best.bw=best.bw,CV_MSEs=CV_MSEs,fold_MSEs=fold_MSEs))
}
"k-fold cross-validation on lienar models given as a vector (or list) of model fomrulae. Return the
CV MSE (Mean mean squared error), not the parameter estimates on each fold."
cv.lm <- function(data, formulae, nfolds = 5) {
    data <- na.omit(data)
    formulae <- sapply(formulae, as.formula)
    n <- nrow(data)
    fold.labels <- sample(rep(1:nfolds, length.out = n))
    mses <- matrix(NA, nrow = nfolds, ncol = length(formulae))
    colnames <- as.character(formulae)
    for (fold in 1:nfolds) {
        test.rows <- which(fold.labels == fold)
        train <- data[-test.rows, ]
        test <- data[test.rows, ]
        for (form in 1:length(formulae)) {
            current.model <- lm(formula = formulae[[form]], data = train)
            predictions <- predict(current.model, newdata = test)
            test.responses <- eval(formulae[[form]][[2]], envir = test)
            test.errors <- test.responses - predictions
            mses[fold, form] <- mean(test.errors^2)
        }
}
    return(colMeans(mses))
}
