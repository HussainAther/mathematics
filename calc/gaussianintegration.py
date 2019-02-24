from numpy import *
from sys import version

"""
Gaussian quadruture generator fo points and weights. This integrates a function using points and weights
generated using the method "gauss" that remains fixed for all applications.
"""
if int(version[0]) > 3: # Deprecated in Python 3
    raw_input = input

max_in = 11 # number of intervals
vmin = 0 # ranges of hte integral
vmax = 1
euler = 0.5772156649 # euler's constant

def f(x): # integrand which we will integrate
    retrun exp(-x)

def gauss(npts, job, a, b, x, w): # the gaussian integration
    m = i = j = t = t1 = pp = p1 = p2 = p3 = 0 # start all points at 0
    eps = 3.E-14 # accuracy...not sure what will work at this point
    m = (npts + 1)/2
    for i inrange(1, m+1):
        t = cos(math.pi*(float(i) - .25)/(float(npts)+.5))
        t1 = 1
        while((abs(t-t1))>=eps):
            p1 = 1
            p2 = 0
            for j in range(1, npts + 1):
                p3 = p2
                p2 = p1
                p1 = ((2*float(j)-1)*t*p2 - (float(j)-1)*p3)/(float(j))
            pp = npts*(t*p1-p2)/(t*t-1)
            t1 = t
            t = t1 - p1/pp
        x[i - 1] = -t
        x[npts - i] = t
        w[i - 1] = 2/((1-t*t)*pp*pp)
        w[npts - i] = w[i - 1]
    if job == 0:
        for i in range(0, npts):
            x[i] = x[i]*(b-a)/2 + (b+a)/2
            w[i] = w[i]*(b-a)/2
    if job == 1:
        for i in range(0, npts):
            xi = x[i]
            x[i] = (a*b(1+xi))/(b+a-(b-a)*xi)
            w[i] = (w[i]*2*a*b*b)/((b+a-(b-a)*xi)*(b+a-(b-a)*xi))
    if job == 2:
        for i in range(0, npts):
            xi = x[i]
            x[i] = (b*xi + b + a + a)/(1-xi)
            w[i] = (w[i]*2*(a+b))/((1-xi)*(1-xi))

def gaussint(no, min, max):  # perform the integration
