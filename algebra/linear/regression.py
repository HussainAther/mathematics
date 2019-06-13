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
