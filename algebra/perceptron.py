import numpy as np

"""
Rosenblatt's pecreptron is an example of a linear discriminant model.

It uses a two-class model with an input vector x transformed using a fixed nonlinear
transformation to give a feature vector phi(x) and create a generalized linear model
of the form

y(x) = f(w^T*phi(x))

with a nonlinear activation function f(.) with as a step function:

f(a) 1 when a >=0 and -1 when a < 0.
"""

def predict(row, weights):
    """
    Make predcitions by evaluating candidate weight values in stoachastic
    gradient descent. After the model is finalized we start making predictions on test data.
    """
    activation = weights[0]
    for i in range(len(row)-1):
        activation += weights[i + 1] * row[i]
    return 1.0 if activation >= 0.0 else 0.0

data =[ # example data in the format [X1, X2, Y]
[2.7810836, 2.550537003, 0]
[1.465489372, 2.362125076, 0]
[3.396561688, 4.400293529, 0]
[1.38807019, 1.850220317, 0]
[3.06407232, 3.005305973, 0]
[7.627531214, 2.759262235, 1]
[5.332441248, 2.088626775, 1]
[6.922596716, 1.77106367, 1]
[8.675418651, -0.242068655,1]
[7.673756466,3.508563011,1]]

weights = [-0.1, 0.20653640140000007, -0.23418117710000003]
for row in data:
    prediction = predict(row, weights)
    print("Expected=%d, Predicted=%d" % (row[-1], prediction))

# model an activation equation
activation = (w1 * X1) + (w2 * X2) + bias


# Estimate Perceptron weights using stochastic gradient descent
def train_weights(train, l_rate, n_epoch):
    weights = [0.0 for i in range(len(train[0]))]
    for epoch in range(n_epoch):
        sum_error = 0.0
        for row in train:
            prediction = predict(row, weights)
            error = row[-1] - prediction
            sum_error += error**2
            weights[0] = weights[0] + l_rate * error
            for i in range(len(row)-1):
                weights[i + 1] = weights[i + 1] + l_rate * error * row[i]
        print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, l_rate, sum_error))
    return weights

def train_weights(train, l_rate, n_epoch):
    """
    Use stochastic gradient descent to estimate weights.
    First we loop over each epoch. Then we loop over each row in the training
    data for an epoch. Then we loop over each weight and update it for a
    rwo in an epoch.
    """
    weights = [0.0 for i in range(len(train[0]))]
    for epoch in range(n_epoch):
        sum_error = 0.0
        for row in train:
            prediction = predict(row, weights)
            error = row[-1] - prediction
            sum_error += error**2
            weights[0] = weights[0] + l_rate * error
            for i in range(len(row)-1):
                weights[i + 1] = weights[i + 1] + l_rate * error * row[i]
        print('>epoch=%d, lrate=%.3f, error=%.3f' % (epoch, l_rate, sum_error))
    return weights

"""
We use an alternative error function known as the perceptron criterion.
"""

def pcrit(w, phi, t):
    """
    Using the t of {-1, +1} target codign scheme we want all patterns to satisfy
    w^T*phi(x_n)*t_n > 0 .
    """
    result = 0
    for n in range(M):
        
