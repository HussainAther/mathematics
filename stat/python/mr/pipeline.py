import numpy as np

"""
Multivariate regression pipeline
"""

def normalize(features):
    """
    features     -   (200, 3)
    features.T   -   (3, 200)

    We transpose the input matrix, swapping
    cols and rows to make vector math easier
    """
    for feature in features.T:
        fmean = np.mean(feature)
        frange = np.amax(feature) - np.amin(feature)

        # Vector subtraction
        feature -= fmean

        # Vector division
        feature /= frange

    return features

def predict(features, weights):
    """
    Form predictions based on features and weights.
    features - (200, 3)
    weights - (3, 1)
    predictions - (200,1)
    """
    predictions = np.dot(features, weights)
    return predictions

# Initialize weights.
W1 = 0.0
W2 = 0.0
W3 = 0.0
weights = np.array([
    [W1],
    [W2],
    [W3]
])

def costfunction(features, targets, weights):
    """
    features:(200,3)
    targets: (200,1)
    weights:(3,1)
    returns average squared error among predictions
    """
    N = len(targets)

    predictions = predict(features, weights)

    # Matrix math lets use do this without looping.
    sqerror = (predictions - targets)**2

    # Return average squared error among predictions.
    return 1.0/(2*N) * sqerror.sum()

def updateweights(features, targets, weights, lr):
    """
    Features:(200, 3)
    Targets: (200, 1)
    Weights:(3, 1)
    """
    predictions = predict(features, weights)

    # Extract our features.
    x1 = features[:,0]
    x2 = features[:,1]
    x3 = features[:,2]

    # Use matrix cross product (*) to simultaneously
    # calculate the derivative for each weight.
    d_w1 = -x1*(targets - predictions)
    d_w2 = -x2*(targets - predictions)
    d_w3 = -x3*(targets - predictions)

    # Multiply the mean derivative by the learning rate
    # and subtract from our weights (remember gradient points in direction of steepest ASCENT).
    weights[0][0] -= (lr * np.mean(d_w1))
    weights[1][0] -= (lr * np.mean(d_w2))
    weights[2][0] -= (lr * np.mean(d_w3))

    return weights
