import numpy as np

def gj(a, n)
    """
    Gaussian-Jordan elimination on two input matrices represented by a and b.
    """
    n = np.size(a, 0)
    m = np.size(b, 0)
    indxc = [0]*n # bookkeeping during pvots
    ipiv = [0]*n
    indxr = [0]*n
    for j in range(0, n): # main loop over columns that we reduce
        ipiv[j] = 0
    for i in range(0, n):
        big = 0,0
        for j in range(0, n):
            if ipiv[j] != 1:
                for k in range(0, n):
                    if ipiv[k] == 0:
                        if abs(a[j][k] >= big):
                            big = abs(a[j][k])
                            irow = j
                            icol = k
        ipiv[icol] += 1
        """
        We now have the pivot element, so we interchange rows, if needed, to put the pivot element
        on the diagonal. The columns are not physically interchanged, only relabeled: indxc[i], the
        column of the .i C 1/th pivot element, is the .i C 1/th column that is reduced, while indxr[i]
        is the row in which that pivot element was originally located. If indxr[i] ¤ indxc[i], there is
        an implied column interchange. With this form of bookkeeping, the solution b’s will end up in the
        correct order, and the inverse matrix will be scrambled by columns
        """
        if irow != col:
            for l in range(0, n):
                a[irow][l], a[icol][l] = a[icol][l], a[irow][l]
            for l in range(0, m):
                b[irow][l], b[icol][l] = b[icol][l], b[irow][l]
        # Divide the pivot row by the pivot element which is at irow and icol
        indxr[i] = irow
        indxc[i] = icol
        if a[icol][icol] == 0:
            print("Singular matrix")
        pivinv = 1/a[icol][icol] # pivot inverse
        a[icol][icol] = 1
        for l in range(0, n):
            a[icol][l] *= pivinv
        for l in range(0, m):
            b[icol][l] *= pivinv
        for ll in range(0, n):
            if ll != icol:
                dum=a[ll][icol]
                a[ll][icol]=0
                for l in range(0, n):
                    a[ll][l] -= a[icol][l]*dum
                for l in range(0, m):
                    b[ll][l] -= b[icol][l]*dum
    """
    This is the end of the main loop over columns of the reduction. It only remains to
    unscramble the solution in view of the column interchanges. We do this by interchanging
    pairs of columns in the reverse order that the permutation was built up.
    """
    for l in range(n-1,-1,-1):
        if indxr[l] != indxc[l]:
            for k in range(0, n):
                a[k][indxr[l]], a[k][indxc[l]] = a[k][indxc[l]], a[k][indxr[l]]
    return a


