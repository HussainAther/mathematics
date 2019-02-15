import numpy as np
import math

"""
Stochastic Gradient Boosting
As mentioned in Friedman et al. (2000) ("Additive logistic regression: a statistical view of boosting")
worked to provide statistical insight of the AdaBoost algorithm. For the classification problem, they
showed that it could be interpreted as a forward stagewise additive model that minimizes an exponential
loss function. This framework led to algorithmic generalizations such as Real AdaBoost, Gentle AdaBoost,
and LogitBoost. Subsequently, these generalizations were put into a unifying framework called gradient boosting machines.
"""

# Initialized all predictions to the sample log-odds: f(0) = log p^ / (i 1−p^)

f0 = math.log(p_hat)

for iteration j = 1...M do
Compute the residual (i.e. gradient) z_i = y_i − p_i
Randomly sample the training data
Train a tree model on the random subset using the residuals as the outcome
Compute the terminal node estimates of the Pearson residuals:
  i
1 / n i
p􏰁 i ( 1 − p􏰁 i )
1 / n 􏰃 n ( y i − p􏰁 i )
i r= 􏰃n
7 Update the current model using fi = fi + λf (j) i
8 end

Algorithm
