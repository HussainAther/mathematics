import numpy as np
import matplotlib.pyplot as plt
import math
import random
import tensorflow as tf

from tensorflow import keras

"""
Stochastic Gradient Boosting
As mentioned in Friedman et al. (2000) ("Additive logistic regression: a statistical view of boosting")
worked to provide statistical insight of the AdaBoost algorithm. For the classification problem, they
showed that it could be interpreted as a forward stagewise additive model that minimizes an exponential
loss function. This framework led to algorithmic generalizations such as Real AdaBoost, Gentle AdaBoost,
and LogitBoost. Subsequently, these generalizations were put into a unifying framework called gradient boosting machines.
"""

# Simple gradient boosting for classification (2-class)

# Initialized all predictions to the sample log-odds: f(0) = log p^ / (1−p^)

f0 = math.log((p_hat / (1 - p_hat))

def gradient(x):
    return

for j in range(1, M+1):
    z_i = y_i − phat_i # Compute the residual (i.e. gradient) z_i = y_i − p_i
    random_data = random.sample(data, len(data) / 10) # Randomly sample the training data
    model.fit(random_data, data_labels, epochs=5) # Train a tree model on the random subset using the residuals as the outcome
    terminal = ((1/n)*sum(y_i - phat_i) / (1/n)*sum(phat_i*(1 - phat_i)) # Compute the terminal node estimates of the Pearson residuals:
    fi = fi + λ*f_i # Update the current model using fi = fi + λf (j) i

