import sys

"""
Given p-values (pvalue p value), we can adjust them for multiple comparisons. We do
this to contorl the false positive (type 1 Type I) error rate or false discovery rate
(FDR fdr). 
"""

p = {4.533744e-01, 7.296024e-01, 9.936026e-02, 9.079658e-02, 1.801962e-01,
     8.752257e-01, 2.922222e-01, 9.115421e-01, 4.355806e-01, 5.324867e-01,
     4.926798e-01, 5.802978e-01, 3.485442e-01, 7.883130e-01, 2.729308e-01,
     8.502518e-01, 4.268138e-01, 6.442008e-01, 3.030266e-01, 5.001555e-02,
     3.194810e-01, 7.892933e-01, 9.991834e-01, 1.745691e-01, 9.037516e-01,
     1.198578e-01, 3.966083e-01, 1.403837e-02, 7.328671e-01, 6.793476e-02,
     4.040730e-03, 3.033349e-04, 1.125147e-02, 2.375072e-02, 5.818542e-04,
     3.075482e-04, 8.251272e-03, 1.356534e-03, 1.360696e-02, 3.764588e-04,
     1.801145e-05, 2.504456e-07, 3.310253e-02, 9.427839e-03, 8.791153e-04,
     2.177831e-04, 9.693054e-04, 6.610250e-05, 2.900813e-02, 5.735490e-03}

def pminf(a):
    """
    For an inupt array a, create a list of minimum vlaues.
    """
    x = 1
    pmin_list = []
    N = len(a)
    for index in range(N):
        if aindex] < x:
            pmin_list.insert(index, a[index])
        else:
            pmin_list.insert(index, x)
    return pmin_list

def cumminf(a):
    """
    Cumulative minimum function of p-values for an array a.
    """
    cummin = []
    cumulative_min = a[0]
    for p in array:
        if p < cumulative_min:
            cumulative_min = p
        cummin.append(cumulative_min)
    return cummin

def cummaxf(a):
    """
    Cumulative maximum function of p-values for an array a.
    """
    cummax = []
    cumulative_max = a[0]
    for e in array:
        if e > cumulative_max:
            cumulative_max = e
        cummax.append(cumulative_max)
    return cummax
