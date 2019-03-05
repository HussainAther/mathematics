import numpy as np
import matplotlib.pyplot as plt

from scipy.ndimage.interpolation import rotate

"""
Jacobi's method is a way of computing eigenvalues and eigenvectors of a real symmetric matrix.

We use a series of linear equations to multiple the elemnets of the matrix a.

It uses off-diagonal elements of a matrix and zeros them by a series of plane rotations. We look at the
rotational angle phi as a functional element of theta in:

theta = cot(2*phi) = c^2 - s^2 / (2sc)
"""

def eigsrt(d, v):
    """
    Given the eigenvalues d[0...n-1] and optionaly the eigenveectors v[0...n-1] as determined by Jacobi,
    this sorts the eigenvalues into descending order and rearranges the columns of matrix v correspondingly.
    """
    k=i
    n = len(d)
    for i in range(0, n):
        k = i
        p = d[i]
        for j in range(i, n+1):
            if d[j] >= p:
                p = d[k]
            if k != i:
                d[k] = d[i]
                d[i] = p
                if v != None:
                    for j in range(0, n+1):
                        p = v[j][i]
                        v[j][i] = v[j][k]
                        v[j][k] = p
    return v


def jacobiNP(A,b,N=25,x=None):
    """Solves the equation Ax=b via the Jacobi iterative method."""
    # Create an initial guess if needed
    if x is None:
        x = np.zeros(len(A[0]))

    # Create a vector of the diagonal elements of A
    # and subtract them from A
    D = np.diag(A)
    R = A - np.diagflat(D)

    # Iterate for N times
    for i in range(N):
        x = (b - np.dot(R,x)) / D
    return x


def jacobi(a):
    """
    Compute all eigenvalues and eigenvectors of a real symmetric matrix a of side-length n and output
    d[0...n-1] that has the eigenvalues of a sorted into descending order while v[0...n-1][0...n-1] is a
    matrix whose columns contain the corresponding nromalized eigenvectors. nrot is the number of the Jacobi rotations
    that are required. Only the upper tirangle of a is accessed.
    """
    eps = 1e-9 # (epsilon) accuracy
    theta = np.radians(30)
    nrot = 0
    if np.size(a,0) != np.size(a,1):
        print("Error: matrix must be symmertic. E.g., of shape nxn")
        return
    n = np.size(a,0)
    v = np.matrix([0]*n,[0]*n)
    np.fill_diagonal(v, 1.0)
    b = np.diagonal(v) # b and d are diagonals that we initialize for convenience
    d = np.diagonal(v)
    z = np.zeros(n)
    for i in range(1,51):
        sm = 0 # sum the magnitude of off-diagonal elements
        for ip in range(0, n):
            for iq in range(ip+1, n+1):
                sm += abs(a[ip][iq])
        if sm == 0:
            eigsrt(d, v)
            return v
        if i < 4:
            tresh =  .2*sm(n**2)
        else:
            tresh = 0
        for ip in range(0,n):
            for eq in range(ip+1, n+1):
                g = 100*abs(a[ip][iq])
                if i > 4 and g <= eps*abs(d[ip]) and g <= eps*abs*d[iq]: # after 4 sweeps, skip rotation if the off-diagonal element is small.
                    a[ip][iq] = 0
                elif abs(a[ip][iq]) > tresh:
                    h = d[iq] - d[ip]
                    if g <= eps*abs(h):
                        t = a[ip][iq]/h
                    else:
                        theta = .5*h/(a[ip][iq])
                        t = 1.0/(abs(theta) + np.sqrt(1+theta**2))
                        if theta < 0: # reverse direction
                            t = -t
                    c = 1.0/np.sqrt(1+t**2)
                    s = t*c
                    tau = s/(1.0+c)
                    h = t*a[ip][iq]
                    z[ip] -= h
                    z[iq] += h
                    d[ip] -= h
                    a[ip][iq] = 0
                    # perform the rotations
                    for j in range(0, ip):
                        rotate(a, j, s)
                        rotate
                    nrot += 1


    return v, nrot


