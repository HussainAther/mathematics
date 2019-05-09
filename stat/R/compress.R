"This case study will focus on the prediction of optimal formulations 
of concrete mixture-based data from designed experiments.
Concrete is an integral part of most industrialized societies. It 
is used to some extent in nearly all structures and in many roads. 
One of the main properties of interest (beside cost) is the compressive 
strength of the hard- ened concrete. The composition of many concretes 
includes a number of dry ingredients which are mixed with water and 
then are allowed to dry and harden. Given its abundance and critical 
role in infrastructure, the composition is important and has been 
widely studied. In this chapter, models will be created to help 
find potential recipes to maximize compressive strength.
We describe a standard type of experimental setup for this scenario 
called a mixture design. Here, boundaries on the upper and lower 
limits on the mixture proportion for each ingredient are used to 
create multiple mixtures that methodically fill the space within 
the boundaries. For a specific type of mixture design, there is a 
corresponding linear regression model that is typically used to model 
the relationship between the ingredients and the outcome. These linear 
models can include interaction effects and higher-order terms for the 
ingredients. The ingredients used in Yeh (2006) were cement (kg/m3), 
fly ash (kg/m3), small particles produced by burning coal, blast furnace 
slag (kg/m3), and water (kg/m3)"
library(AppliedPredictiveModeling)
data(concrete)
str(concrete)
str(mixtures)
featurePlot(x = concrete[, -9],
            y = concrete$CompressiveStrength,
            ## Add space between panels
            between = list(x=1, y=1),
            ## Add background grid ('g') and a smoother ('smooth')
            type = c("g", "p", "smooth"))
averaged <- ddply(mixtures,
                .(Cement, BlastFurnaceSlag, FlyAsh, Water,
                  Superplasticizer CoarseAggregate,
                  FineAggregate, Age),
                  function(x) c(CompressiveStrength = mean(x$CompressiveStrength)))
set.seed(100)
forTraining <- createDataPartition(averaged$CompressiveStrength,
                                   p = 3/4)[[1]]
trainingSet <- averaged[ forTraining,]
testSet <- averaged[-forTraining,]
"Formula we use for modeling"
modFormula <- paste("CompressiveStrength ~ (.)^2 + I(Comenet^2) + ",
                    "I(BlastFurnaceSlag^2) + I(FlyAsh^2) + I(Water^2) +",
                    "I(Superplasticizer^2) + I(CoarseAggregate^2) + ",
                    "I(FineAggregate^2) + I(Age^2)")
modFormula <- as.formula(modFormula)
"10-fold cross-validation"
controlObject <- trainControl(method = "repeatedcv", 
                              repeats = 5,
                              number 10)
set.seed(100)
"Linear regression to create same folds"
linearReg <- train(modFormula,
                   data = trainingSet,
                   method = "lm",
                   trControl = controlObject)
linearReg
set.seed(100)
"Other two linear models"
plsModel <- train(modForm, data = trainingSet,
                  method = "pls",
                  prePoc = c("center", "scale"),
                  tuneLength = 15,
                  trControl = controlObject)
enetGrid <- expand.grid(.lambda = c(0, .001, .01, .1),
                        .fraction = set(.05, 1, length=20))
enetModel <- train(modForm, data = trainingSet,
                   method = "enet",
                   preProc = c("center", "scale"),
                   tuneGrid = enetGrid,
                   trControl = controlObject)
"MARS, neural networks and SVMs"
earthModel <- train(CompressiveStrength ~ ., data = trainingSet,
                    method = "earth",
                    tuneGrid = expand.grid(.degree = 1,
     		                           .prune = 2:25),
                    trControl = controlObject)
svmRModel <- train(CompressiveStrength ~ ., data = trainingSet,
                   method = "svmRadial",
                   tuneLength = 15,
                   preProc = c("center", "scale"),
                   trControl = controlObject)
nnetGrid <- expand.grid(.decay = c(.001, .01, .1),
                        .size = seq(1, 27, by = 2),
                        .bag = FALSE)
nnetModel <- train(CompressiveStrength ~ .,
                   data = trainingSet,
                   method = "avNNet",
                   tuneGrid = nnetGrid,
                   preProc = c("center", "scale"),
                   linout = TRUE,
                   trace = FALSE,
                   maxit = 1000,
                   trControl = controlObject)
"Regression and model trees"
rpartModel <- train(CompressiveStrength ~ .,
                    data = trainingSet,
                    method = "rpart",
                    tuneLength = 30,
                    trControl = controlObject)
ctreeModel <- train(CompressiveStrength ~ .,
                    data = trainingSet,
                    method = "ctree",
                    tuneLength = 10,
                    trControl = controlObject)
mtModel <- train(CompressiveStrength ~ .,
                 data = trainingSet,
                 method = "M5",
                 trControl = controlObject)
"Remaining model objetcs"
treebagModel <- train(CompressiveStrength ~ .,
                      data = trainingSet,
                      method = "treebag",
                      trControl = controlObject)
rfModel <- train(CompressiveStrength ~ .,
                 data = trainingSet,
                 method = "rf",
                 tuneLength = 10,
                 ntrees = 1000,
                 importance = TRUE,
                 trControl = controlObject)
gbmGrid <- expand.grid(.interaction.depth = seq(1, 7, by =2),
                       .n.trees = seq(100, 1000, by = 50),
                       .shrinkage = c(.01, .1))
gbmModel <- train(CompressiveStrength ~ .,
                  data = trainingSet,
                  method = "gbm",
                  tuneGrid = gbmGrid,
                  verbose = FALSE,
                  trControl = controlObject)
cubistGrid <- expand.grid(.committees = c(1, 5, 10, 50, 75, 100),
                          .neighbors = c(0, 1, 3, 5, 7, 9))
cbModel <- train(CompressiveStrength ~ .,
                 data = trainingSet,
                 method = "cubist",
                 tuneGrid = cubistGrid,
                 trControl = controlObject)
"Resampling results"
allResamples <- resamples(list("Linear Reg" = lmModel,
                               "PLS" = plsModel,
                               "Elastic Net" = enetModel,
                               MARS = earthModel,
                               SVM = svmRModel,
                               "Neural Networks" = nnetModel,
                               CART = rpartModel,
                               "Cond Inf Tree" = ctreeModel,
                               "Bagged Tree" = treebagModel,
                               "Boosted Tree" = gbmModel,
                               "Random Forest" = rfModel,
                               Cubist = cbModel))
"Plot the RMSE values"
parallelPlot(allResamples)
"Use R-squared"
parallelplot(allResamples, metric = "Rsquared")
nnetPredictions <- predict(nnetModel, testData)
gbmPredictions <- predict(gbmModel, testData)
cbPredictions <- predict(cbModel, testData)
"Use 28-day data to generate a set of random starting points from the training set."
age28Data <- subset(trainingData, Age == 28)
"Remove the age and compressive strength columns and then center and scale the predictor columns."
pp1 <- preProcess(age28Data[, -(8:9)], c("center", "scale"))
scaledTrain <- predict(pp1, age28Data[, 1:7])
"Use a single random mixutre to initialize the maximum dissimilarity sampling process."
startMixutre <- sample(1: nrow(age28Data), 1)
starters <- scaledTrain[startMixture, 1:7]
"Select 14 more mixtures to complete a diverse set of starting points for the search algorithms."
pool <- scaledTrain
index <- maxDissim(starters, pool, 14)
startPoints <- c(startMixture, index)
starters <- age28Data[startPoints, 1:7]
"Remove water."
startingValues <- starts[, -4]
"Maximize compressive strength using optim to search the mixture space for optimal formulations.
This minimzies a function so it returns the negative of the compress strength."
modelPrediction <- function(x, mod) {
    ## Check to make sure mixture proportions are in the correct range
    if(x[1] < 0 | x[1] > 1) return(10^38)
    if(x[2] < 0 | x[2] > 1) return(10^38)
    if(x[3] < 0 | x[3] > 1) return(10^38)
    if(x[4] < 0 | x[4] > 1) return(10^38)
    if(x[5] < 0 | x[5] > 1) return(10^38)
    if(x[6] < 0 | x[6] > 1) return(10^38)
    ## Determine water proportion
    x <- c(x, 1 - sum(x))
    ## Check water range
    if(x[7] < .05) return(10^38)
    ## Convert the vector to a data frame, assign names, and fix age at 28 days
    tmp <- as.data.frame(t(x))
    names(tmp) <- c("Cement", "BlastFurnaceSlag", "FlyAsh",
                    "Superplasticizer", "CoarseAggregate",
                    "FineAggregate", "Water")
    tmp$Age <- 28
    ## Model prediction, square to get back to original units, and return the negative
    -predict(mod, tmp)
}
"Predict using cubist model."
cbResults <- startingValues
cbResults$Water <- NA
cbResults$Prediction <- NA
for(i in 1:nrow(cbResults)) {
    results <- optim(unlist(cbResults[i, 1:6]),
                     modelPrediction,
                     method = "Nelder-Mead",
                     ## Use method = "SANN" for simulated annealing
                     control=list(maxit=5000),
                     ## The next option is passed to the modelPrediction() function
                     mod = cbModel)
    ## Save the predicted compressive strength
    cbResults$Prediction[i] <- -results$value
    ## Also save the final mixture values
    cbResults[i, 1:6] <- results$par
}
"Calculate the water proportion."
cbResults$Water <- 1 - apply(cbResults[, 1:6], 1, sum)
"Keep top three mixtures."
cbResults <- cbResults[order(-cbResults$Prediction),][1:3,]
cbResults$Model <- "Cubist"
"For the neural network model."
nnetResults <- startingValues
nnetResults$Water <- NA
nnetResults$Prediction <- NA
for(i in 1:nrow(nnetResults)) {
    results <- optim(unlist(nnetResults[i, 1:6,]),
                     modelPrediction,
                     method = "Nelder-Mead",
                     control=list(maxit5000),
                     mod = nnetModel)
    nnetResults$Prediction[i] <- -results$value
    nnetResults[i, 1:6] <- results$par
}
nnetResults$Water <- 1 - apply(nnetResults[, 1:6], 1, sum)
nnetResults <- nnetResults[order(-nnetResults$Prediction),][1:3,]
nnetResults$Model <- "NNet"
"Principal component analysis (PCA pca principal)."
pp2 <- preProcess(age28Data[, 1:7], "pca")
pca1 <- predict(pp2, age28Data[, 1:7])
pca1$Data <- "Training Set"
pca$Data[startPoints] <- "Starting Values"
pca3 <- predict(pp2, cbResults[, names(age28Data[, 1:7])])
