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
modFormula <- paste("CompressiveStrength ~ (.)^2 + I(Comenet^2) + ",
                    "I(BlastFurnaceSlag^2) + I(FlyAsh^2) + I(Water^2) +",
                    "I(Superplasticizer^2) + I(CoarseAggregate^2) + ",
                    "I(FineAggregate^2) + I(Age^2)")
modFormula <- as.formula(modFormula)
controlObject <- trainControl(method = "repeatedcv", 
                              repeats = 5,
                              number 10)
set.seed(100)
linearReg <- train(modFormula,
                   data = trainingSet,
                   method = "lm",
                   trControl = controlObject)
linearReg
set.seed(100)
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
