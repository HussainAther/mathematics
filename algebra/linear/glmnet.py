import numpy
import matplotlib.pyplot as plot

from sklearn import datasets, linear_model
from math import sqrt
"""

"""

def S(z, gamma):
    """
    Lasso coefficient shrinkage function used as a soft limiter such
    that, if the first input is larger than the second, the output is the
    first input reduced by the magnitude of the second.
    """
    if gamma >= abs(z):
        return 0.0
    return (z/abs(z))*(abs(z) - gamma)

# read data
data = readlines(open("winequality-red", "r"))

xList = []
labels = []
names = []
firstLine = True

for line in data:
    if firstLine:
        names = line.strip().split(";")
        firstLine = False
    else:
        #split on semi-colon
        row = line.strip().split(";")
        #put labels in separate array
        labels.append(float(row[-1]))
        #remove label from row
        row.pop()
        #convert row to floats
        floatRow = [float(num) for num in row]
        xList.append(floatRow)

#Normalize columns in x and labels
nrows = len(xList)
ncols = len(xList[0])
#calculate means and variances
xMeans = []
