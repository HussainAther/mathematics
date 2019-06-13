import numpy as np
import matplotlib.pyplot as plt

def estimate_coef(x,y):
    """
    For variable arrays x and y, estimate the coefficients of linear regression.
    """
    n = np.size(x) # size
  
    m_x, m_y = np.mean(x), np.mean(y) # get the means

    SS_xy = np.sum(y*x) - n*m_y*m_x # cross derivation
    SS_xx = np.sum(x*x) - n*m_x*m_x
  
    b_1 = SS_xy / SS_xx # regression coefficients
    b_0 = m_y - b_1*m_x
  
    return(b_0, b_1)

def plot_regression_line(x, y, b):
    """
    Return the plotted regression line for data arrays x and y with coefficients b.
    """
    plt.scatter(x, y, color = "m", marker = "o", s = 30) # plot the scatterpoints of our data
  
    y_pred = b[0] + b[1]*x # predict the response
  
    plt.plot(x, y_pred, color = "g") # plot the line
    plt.xlabel("x")
    plt.ylabel("y")
    plt.show()

"""
Tensorflow
"""

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
    
from sklearn.utils import shuffle

def model(X, hidden_weights1, hidden_bias1, ow):
    """
    Hidden layer model.
    """
    hidden_layer = tf.nn.sigmoid(tf.matmul(X, hidden_weights1)+ b)
    return tf.matmul(hidden_layer, ow)

dsX = np.linspace(-1, 1, trainsamples + testsamples).tranpose()
dsY = 0.8*pow(dsX,2)+2*dsX+np.random.randn(*dsX.shape)*.22+.8

X = tf.placeholder("float")
Y = tf.placeholder("float")

# Create first hidden layer.
hw1 = tf.Variable(tf.random_normal([1, 10], stddev=0.1))

# Create output connection.
ow = tf.Variable(tf.random_normal([10, 1], stddev=0.0))

# Create bias.
b = tf.Variable(tf.random_normal([10], stddev=0.1))
model_y = model(X, hw1, b, ow)

# Cost function.
cost = tf.pow(model_y-Y, 2)/(2)

# Construct an optimizer.
train_op = tf.train.GradientDescentOptimizer(0.05).minimize(cost)

# Launch the graph in a session.
epochs = 50
with tf.Session() as sess:
    tf.global_variables_initializer().run() # Initialize all variables.
    for i in range(1, epochs):
        # Randomize the samples to implement a better training.
        dsX, dsY = shuffle(dsX.tranpose(), dsY)
        trainX, trainY = dsX[0:trainsamples], dsY[0:trainsamples]
