import numpy as np

"""
Householder algorithm reduces an n x n matrix A to tridiagonal form by n - 2 orthogonal transformations.
Each transformation annihilates the required part of a whole column and whole corresponding row.
The Householder matrix P has the form:

P = 1 - 2w dot w^T

in which w is a real vector with |w|^2 = 1.
"""

def mult_matrix(M, N):
    """Multiply square matrices of same dimension M and N"""
    tuple_N = zip(*N)

    # Nested list comprehension to calculate matrix multiplication
    return [[sum(el_m * el_n for el_m, el_n in zip(row_m, col_n)) for col_n in tuple_N] for row_m in M]

def trans_matrix(M):
    """Take the transpose of a matrix."""
    n = len(M)
    return [[ M[i][j] for i in range(n)] for j in range(n)]

def norm(x):
    """Return the Euclidean norm of the vector x."""
    return sqrt(sum([x_i**2 for x_i in x]))

def Q_i(Q_min, i, j, k):
    """Construct the Q_t matrix by left-top padding the matrix Q
    with elements from the identity matrix."""
    if i < k or j < k:
        return float(i == j)
    else:
        return Q_min[i-k][j-k]

def householder(A):
    """Performs a Householder Reflections based QR Decomposition of the
    matrix A. The function returns Q, an orthogonal matrix and R, an
    upper triangular matrix such that A = QR."""
    n = len(A)

    # Set R equal to A, and create Q as a zero matrix of the same size
    R = A
    Q = [[0.0] * n for i in xrange(n)]

    # The Householder method
    for k in range(n-1):
        # Create identity matrix of same size as A
        I = [[float(i == j) for i in xrange(n)] for j in xrange(n)]

        # Create the vectors x, e and the scalar alpha
        x = [row[k] for row in R[k:]]
        e = [row[k] for row in I[k:]]
        alpha = -cmp(x[0],0) * norm(x)

        # Using anonymous functions, we create u and v
        u = map(lambda p,q: p + alpha * q, x, e)
        norm_u = norm(u)
        v = map(lambda p: p/norm_u, u)

        # Create the Q minor matrix
        Q_min = [ [float(i==j) - 2.0 * v[i] * v[j] for i in xrange(n-k)] for j in xrange(n-k) ]

        # "Pad out" the Q minor matrix with elements from the identity
        Q_t = [[ Q_i(Q_min,i,j,k) for i in xrange(n)] for j in xrange(n)]

        # If this is the first run through, right multiply by A,
        # else right multiply by Q
        if k == 0:
            Q = Q_t
            R = mult_matrix(Q_t,A)
        else:
            Q = mult_matrix(Q_t,Q)
            R = mult_matrix(Q_t,R)

    return trans_matrix(Q), R

def houseVector(x):
    """
    Return the Householder vector of size x.
    """
    n = len(x)
    x = x/norm(x) # Euclidean norm
    s = np.matrix(x[2:n+1], x[2:n+1])
    v = x[2:n+1]
    if s == 0:
        beta = 0
    else:
        mu = np.sqrt(x[0]**2 + s)
        if x[0] <= 0:
            v[0] = x[0] - mu
        else:
            v[0] = -s/(x[0] + mu)
        beta = 2*v[0]**2

"""
We can find a Hessenberg matrix using the Householder method. Hessenberg matrix is (almost) the Schur triangular form of a matrix.
Shur triangular is a matrix that's unitarilty equivalent to an upper triangular matrix whose diagonal elements are the eigenvalues of the original matrix.
The upper Hessenberg matrix has zero entries below the first subdiagonal, and the lower one has zero entries above the first superdiagonal.
"""
def housHess(a):
    """
    Householder-Hessenberg method outputs a Hessenberg matrix on some numpy matrix a.
    """
    n = max(np.size(a,1), np.size(a,0)) # find the number of rows/columns (whichever is greater)
    q = np.identity(n) # get the identity matrix of size n
    h = a
    for k in range(1, n-1): # iterate through each row/column except the last two
        [v,beta] =
