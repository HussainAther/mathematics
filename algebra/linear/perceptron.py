import numpy as np

from keras.models import Sequential
from keras.layers import Dense

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
    Make predictions by evaluating candidate weight values in stoachastic
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
            prediction = predict(row, weights) # scoring for a summation of the prediction
            error = row[-1] - prediction # this is the perceptron criterion
            sum_error += error**2 # sum the error
            weights[0] = weights[0] + l_rate * error
            for i in range(len(row)-1):
                weights[i + 1] = weights[i + 1] + l_rate * error * row[i]
        print(">epoch=%d, lrate=%.3f, error=%.3f" % (epoch, l_rate, sum_error))
    return weights

"""
Multi-layer perceptron MLP mlp
"""

def split_sequences(sequences, n_steps):
    """
    Split a multivariate sequence or sequences into samples.
    """
    X, y = list(), list()
    for i in range(len(sequences)):
        # find the end of this pattern
	end_ix = i + n_steps
	# check if we are beyond the dataset
	if end_ix > len(sequences)-1:
	    break
	# gather input and output parts of the pattern
	seq_x, seq_y = sequences[i:end_ix, :], sequences[end_ix, :]
	X.append(seq_x)
	y.append(seq_y)
    return np.array(X), np.array(y)

# Initialize input sequence
in_seq1 = array([10, 20, 30, 40, 50, 60, 70, 80, 90])
in_seq2 = array([15, 25, 35, 45, 55, 65, 75, 85, 95])
out_seq = array([in_seq1[i]+in_seq2[i] for i in range(len(in_seq1))])

# Convert to [rows, columns] structure
in_seq1 = in_seq1.reshape((len(in_seq1), 1))
in_seq2 = in_seq2.reshape((len(in_seq2), 1))
out_seq = out_seq.reshape((len(out_seq), 1))

# Horizontally stack columns
dataset = np.hstack((in_seq1, in_seq2, out_seq))
# choose a number of time steps
n_steps = 3

# Convert into input/output
X, y = split_sequences(dataset, n_steps)

# flatten input
n_input = X.shape[1] * X.shape[2]
X = X.reshape((X.shape[0], n_input))
n_output = y.shape[1]

# Define model
model = Sequential()
model.add(Dense(100, activation="relu", input_dim=n_input))
model.add(Dense(n_output))
model.compile(optimizer="adam", loss="mse")

weights = train_weights(X, .01, 100)

# Fit model
model.fit(X, y, epochs=2000, verbose=0)

# Predict
x_input = array([[70,75,145], [80,85,165], [90,95,185]])
x_input = x_input.reshape((1, n_input))
yhat = model.predict(x_input, verbose=0)
predict(weights)
