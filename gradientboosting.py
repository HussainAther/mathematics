import numpy as np

"""
Stochastic Gradient Boosting
As mentioned in Sect. 8.6, Friedman et al. (2000) worked to provide statis- tical insight of the
AdaBoost algorithm. For the classification problem, they showed that it could be interpreted as a
forward stagewise additive model that minimizes an exponential loss function. This framework led to
algorithmic generalizations such as Real AdaBoost, Gentle AdaBoost, and LogitBoost. Subsequently,
these generalizations were put into a unifying framework called gradient boosting machines.
"""

# Initialized all predictions to the sample log-odds: f(0) = log p^ / (i 1−p^)
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
