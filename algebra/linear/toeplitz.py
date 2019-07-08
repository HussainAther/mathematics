"""
Find out if a matrix is Toeplitz (toeplitz) or not for some matrix m.
"""

col = len(mat[0]) # columns
row = len(mat) # rows

def checkDiag(mat, i, j):
    """
    Check if all elements present in the descending diagonal
    starting from position (i, j) in the matrix are all the same
    or not.
    """
    res = mat[i][j]
    i += 1
    j += 1
    while i < col and j < row:
        if mat[i][j] != res:
            return False
        i += 1
        j += 1
    return True

def isToeplitz(mat):
    """
    Check whether the matrix is Toeplitz using our routine.
    """
    for j in range(row):
        if not checkDiag(mat, 0, j):
            return False
    for i in range(1, col):
        if not checkDiag(mat, i, 0):
            return False
    return True
