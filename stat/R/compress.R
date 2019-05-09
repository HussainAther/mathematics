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
