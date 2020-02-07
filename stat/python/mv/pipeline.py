import numpy as np

"""
Create a normalized matrix of the shape of the data.
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
