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
        indxr[i] = irow
        # Divide the pivot row by the pivot element which is at irow and icol


