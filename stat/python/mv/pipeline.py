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
