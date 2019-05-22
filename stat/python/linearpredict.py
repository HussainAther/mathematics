import emcee
import pymc
import pystan
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns; sns.set()

from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.linear_model import Lasso, LinearRegression, Ridge
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import PolynomialFeatures

"""
Linear prediction uses data points equally spaced along a line such that we use
values to autocorrelate and predict based on them.

This is the maximum entropy method (MEM) with all poles. We can adjust various values of m in our
linear prediction.
"""

def MEM(a, m=5):
    """
    Takes a vector of list a. Return the mean square discrepancy as xms and m linear prediction coefficients
    as a list d.
    """
    d = [0]*m
    p = 0
    n = len(a)
    wk1 = [0]*len(n)
    wk2 = [0]*len(n)
    wkm = [0]*len(m)
    for j in range(0, n):
        p += np.sqrt(a[j])
    xms = p/n
    wk1[0] = a[0]
    wk2[n-2] = a[n-1]
    for j in range(1, n-1):
        wk1[j] = a[j]
        wk2[j-1] = a[j]
    for k in range(0, m):
        num = 0 # numerator
        den = 0 # denominator
        for j in range(0, n-k):
            num += wk[j]*wk2[j]
            den += np.sqrt(wk1[j]) + np.sqrt(wk2[j])
        d[k] = 2*num/den
        xms *= (1-np.sqrt(d[k]))
        for i in range(0, k):
            d[i] = wkm[i] - d[k] * wkm[k-i-1]
            # recursive algorithm building up the answer for larger and
            # larger values of m until the desiredf value is achieved.
        if k == m-1:
            return xms, d
        for i in range(0, k+1):
            wkm[i] = d[i]
        for j in range(0, n-k-1):
            wk1[j] -= wkm[j]*wk2[j]
            wk1[j] = wk2[j+1] - wkm[k]*wk1[j+1]
    return xms, d

"""
We can extrapolate the autocorrelation function to lags larger than M (the order or number of poles of the approximation).

The MEM estimation is a function of continously varying frequency f. Given the coefficients it computes,
we will create a function that evaluates and returns the estimated power spectrum as a functon
of f*delta (with delta being the sampling interval). The sampling interval describes the space between
the spectral features of the frequency.

From MEM, we can create a power spectrum estimate as a function fdt = f*delta. f*delta
should lie in the Nyquist range between -1/2 and 1/2.
"""

def PSE(xms, d, *fdt):
    """
    Given xms and d from the MEM function, this function returns power spectrum estimate
    as a function of fdt = f*delta. fdt is the optional frequency scale we use.
    """
    if not fdt:
        fdt = 1
    smr = 1
    sumi = 1
    wr = 1
    wr = 0
    m = len(d)
    theta = 2*np.pi*fdt
    wpr = np.cos(theta)
    wpi = np.sin(theta)
    for i in range(0, m):
        wtemp = wr
        wr = wtemp * wpr - wi* w pi
        wi = wi * wpr + wtemp * wpi
        sumr -= d[i] * wr
        sumi -= d[i] * wi
    return xms/(sumr*sumr + sumi*sumi)

"""
We can remove the bias in linear prediction by noticing that the linear prediction coefficients
are computed using the quantized data, and that the discrepancy is also quantized.
We can compute the residuals by takign advantage of how the smaller values of
discrepancy will occur more fequently than larger ones. This is Huffman coding.

The Wiener-Khinchin theorem says the Fourier transform of the autocorrelation is
equal to the power spectrum. This means the Fourier transform is a Laurent series in z.

We must find coefficients that satsify the equation:

a_o / abs(a + summation of k=1 to M of (a_k*z^k)^2 ~ summtion from j = -M to M of phi_j*z^j

The ~ is an apprxoimate equal sign. It means the series expansion on the left sdie is supposed to agree
with the right side term-by-term from z^-M to z^M. Outside of this, the right side is obviously zero
whiel the left size will have nonzero terms.
"""

def period(x, y, ofac=4, hifac):
    """
    Given list of data points x[0...n-1] and ordinates y[0...n-1] and oversampling factor ofac, this
    fills array px[0...nout-1] with increasing sequence of frequencies up to hifac times the "average"
    Nyquist freuqnecy. It fills array py[0...nout-1] with the Lomb normalized periodogram values at those
    frequencies. x and y are not altered. The vectors px and py resize to nout if their initial size is less
    than this. Otherwise the first nout components are filled.
    """
    n = len(x)
    (wi, wpi, wpr, wr, px, py) = ([0]*n, [0]*n, [0]*n, [0]*n, [0]*n)
    nout = int(.5*ofac*hifac*n)
    if np < nout:
        px.np.ndarray.resize(nout)
        py.np.ndarray.resize(nout)
    ave = np.avearge(y)
    var = np.var(y)
    if var == 0:
        print("Zero variacne in period")
        return
    xmax = xmin = x[0]
    for j in range(0, n):
        if x[j] > xmax:
            xmax = x[j]
        if x[j] < xmin:
            xmin = x[j]
    xdif = xmax - xmin
    xave = .5*(xmax+xmin)
    pymax =0
    pnow = 1/(xdif*ofac) # starting frequency
    for j in range(0, n): # initialize values for the trigonometric recurrences at each data point
        arg = 2*np.pi*(x[j]-ave)*pnow
        wpr[j] = -2*np.sqrt(np.sin(.5*arg))
        wpi[j] = np.sin(arg)
        wr[j] = np.cos(arg)
        wi[j] = wpi[j]
    for i in range(0, nout):
        px[i] = pnow
        sumsh = sumc = 0
        for j in range(0,n):
            c = wr[j]
            s = wi[j]
            sumsh += s*c
            sumc += (c-s)*(c+s)
        wtau = .5*np.arctan(p2*sumsh, sumc])
        swtau = np.sin(wtau)
        cwtau = np.cos(wtau)
        sums = sumc= sumsy = sumcy = 0
        for j in range(0, n): # loop over the data again to get the periiodogram value
            s = wi[j]
            c = wr[j]
            ss = s * cwtau - c*swtau
            cc = c*cwtau + s*swtau
            sums += ss*ss
            sumc += cc*cc
            yy = y[j] - ave
            sumsy += yy*ss
            sumcy += yy*cc
            wtemp = wr[j]
            wr[j] = (wtemp*wpr[j] - wr[j] * wpi[j]) + wr[j] # trigonometric recurrences
            wi[j] = (wi[j] * wpr[j] + wtemp * wpi[j]) + wi[j]
        py[i] = .5*(sumcy * sumcy/sumc + sumsy * sumsy/sums)/var
        if py[i] >= pymax:
            jmax = i
            pymax = py[jmax]
        pnow += 1/(ofac*xdif)
    expy = np.exp(-pymax)
    effm = 2*nout/ofac
    prob = effm * expy
    if prob > .01:
        prob = 1 - np.power(1 - expy, effm)
    return px, py, prob

"""
We can also use emcee (MCMC Hammer) and pystan packages to do a line of best fit to our data.
"""

def prior(theta):
    """
    Logarithmic prior used for the log likelihood and log posterior functions for some tuple
    of (alpha, beta, sigma) to define our function as input theta. 
    """
    alpha, beta, sigma = theta
    if sigma < 0:
        return -np.inf  # log(0)
    else:
        return -1.5 * np.log(1 + beta ** 2) - np.log(sigma)

def posterior(theta, x, y):
    """
    Logarithmic posterior using log likelihood and log prior.
    """
    alpha, beta, sigma = theta
    y_model = alpha + beta * x
    """
    Calculate the logarithmic likelihood ll. 
    """
    ll = -0.5 * np.sum(np.log(2 * np.pi * sigma ** 2) + (y - y_model) ** 2 / sigma ** 2)
    return prior(theta) + ll

"""
Linear regression.
"""

rng = np.random.RandomState(1)
x = 10 * rng.rand(50)
y = 2 * x - 5 + rng.randn(50)
plt.scatter(x, y)

model = LinearRegression(fit_intercept=True)

model.fit(x[:, np.newaxis], y)

xfit = np.linspace(0, 10, 1000)
yfit = model.predict(xfit[:, np.newaxis])

plt.scatter(x, y)
plt.plot(xfit, yfit)

rng = np.random.RandomState(1)
X = 10 * rng.rand(100, 3)
y = 0.5 + np.dot(X, [1.5, -2., 1.])

model.fit(X, y)

"""
Polynomial basis functions.
"""

x = np.array([2, 3, 4])
poly = PolynomialFeatures(3, include_bias=False)
poly.fit_transform(x[:, None])

poly_model = make_pipeline(PolynomialFeatures(7), LinearRegression())
rng = np.random.RandomState(1)
x = 10 * rng.rand(50)
y = np.sin(x) + 0.1 * rng.randn(50)

poly_model.fit(x[:, np.newaxis], y)
yfit = poly_model.predict(xfit[:, np.newaxis])

plt.scatter(x, y)
plt.plot(xfit, yfit)

"""
Gaussian basis function.
"""

class GaussianFeatures(BaseEstimator, TransformerMixin):
    """
    Uniformly spaced Gaussian features for one-dimensional input.
    """
    def __init__(self, N, width_factor=2.0):
        """
        Initialize with N number of features.
        """
        self.N = N
        self.width_factor = width_factor
    
    @staticmethod
    def _gauss_basis(x, y, width, axis=None):
        """
        Basis for data in (x, y) format.
        """
        arg = (x - y) / width
        return np.exp(-0.5 * np.sum(arg ** 2, axis))
        
    def fit(self, X, y=None):
        """
        Create N centers spread along the data range.
        """
        self.centers_ = np.linspace(X.min(), X.max(), self.N)
        self.width_ = self.width_factor * (self.centers_[1] - self.centers_[0])
        return self
        
    def transform(self, X):
        """
        Transform using the Gaussian basis.
        """
        return self._gauss_basis(X[:, :, np.newaxis], self.centers_,
                                 self.width_, axis=1)

gauss_model = make_pipeline(GaussianFeatures(20),
                            LinearRegression())
gauss_model.fit(x[:, np.newaxis], y)
yfit = gauss_model.predict(xfit[:, np.newaxis])

plt.scatter(x, y)
plt.plot(xfit, yfit)
plt.xlim(0, 10)

"""
Regularization.
"""

model = make_pipeline(GaussianFeatures(30),
                      LinearRegression())
model.fit(x[:, np.newaxis], y)

plt.scatter(x, y)
plt.plot(xfit, model.predict(xfit[:, np.newaxis]))

plt.xlim(0, 10)
plt.ylim(-1.5, 1.5)

def basis_plot(model, title=None):
    """
    Plot the model basis.
    """
    fig, ax = plt.subplots(2, sharex=True)
    model.fit(x[:, np.newaxis], y)
    ax[0].scatter(x, y)
    ax[0].plot(xfit, model.predict(xfit[:, np.newaxis]))
    ax[0].set(xlabel="x", ylabel="y", ylim=(-1.5, 1.5))
    
    if title:
        ax[0].set_title(title)

    ax[1].plot(model.steps[0][1].centers_,
               model.steps[1][1].coef_)
    ax[1].set(xlabel="basis location",
              ylabel="coefficient",
              xlim=(0, 10))

model = make_pipeline(GaussianFeatures(30), LinearRegression())
basis_plot(model)

"""
Ridge regression.
"""

model = make_pipeline(GaussianFeatures(30), Ridge(alpha=0.1))
basis_plot(model, title="Ridge Regression")

"""
Lasso regression.
"""

model = make_pipeline(GaussianFeatures(30), Lasso(alpha=0.001))
basis_plot(model, title="Lasso Regression")
