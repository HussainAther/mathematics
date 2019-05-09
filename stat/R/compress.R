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
