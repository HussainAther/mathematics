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

# normalize columns in x and labels
nrows = len(xList)
ncols = len(xList[0])

# calculate means and variances
xMeans = []
xSD = []
    for i in range(ncols):
        col = [xList[j][i] for j in range(nrows)]
        mean = sum(col)/nrows
        xMeans.append(mean)
        colDiff = [(xList[j][i] - mean) for j in range(nrows)]
        sumSq = sum([colDiff[i] * colDiff[i] for i in range(nrows)])
        stdDev = sqrt(sumSq/nrows)
        xSD.append(stdDev)

# calculate means and standard deviations to normalize xList
xNormalized = []
    for i in range(nrows):
        rowNormalized = [(xList[i][j] - xMeans[j])/xSD[j] for j in range(ncols)]
        xNormalized.append(rowNormalized)


labelNormalized = [(labels[i] - meanLabel)/sdLabel for i in range(nrows)]

# select value for alpha parameter
alpha = 1.0

# make a pass through the data to determine value of lambda that
# just suppresses all coefficients.
# start with betas all equal to zero.
xy = [0.0]*ncols
for i in range(nrows):
    for j in range(ncols):
        xy[j] += xNormalized[i][j] * labelNormalized[i]

maxXY = 0.0
for i in range(ncols):
    val = abs(xy[i])/nrows
    if val > maxXY:
        maxXY = val

# calculate starting value for lambda
lam = maxXY/alpha


# this value of lambda corresponds to beta = list of 0's
# initialize a vector of coefficients beta
beta = [0.0] * ncols
# initialize matrix of betas at each step

betaMat = []
betaMat.append(list(beta))

# begin iteration
nSteps = 100
lamMult = 0.93 # 100 steps gives reduction by factor of 1000 in
               # lambda (recommended by authors)

nzList = []
for iStep in range(nSteps):
    #make lambda smaller so that some coefficient becomes non-zero
    lam = lam * lamMult

    deltaBeta = 100.0
    eps = 0.01
    iterStep = 0
    betaInner = list(beta)

    while deltaBeta > eps:
        iterStep += 1
        if iterStep > 100: break

        # cycle through attributes and update one-at-a-time
        # record starting value for comparison
        betaStart = list(betaInner)
        for iCol in range(ncols):

