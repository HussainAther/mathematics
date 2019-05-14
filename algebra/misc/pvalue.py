import sys

"""
Given p-values (pvalue p value), we can adjust them for multiple comparisons. We do
this to contorl the false positive (type 1 Type I) error rate or false discovery rate
(FDR fdr). 
"""

# Benjamin-Hochberg (benjamin hochberg) p-values
bhp = [4.533744e-01, 7.296024e-01, 9.936026e-02, 9.079658e-02, 1.801962e-01,
     8.752257e-01, 2.922222e-01, 9.115421e-01, 4.355806e-01, 5.324867e-01,
     4.926798e-01, 5.802978e-01, 3.485442e-01, 7.883130e-01, 2.729308e-01,
     8.502518e-01, 4.268138e-01, 6.442008e-01, 3.030266e-01, 5.001555e-02,
     3.194810e-01, 7.892933e-01, 9.991834e-01, 1.745691e-01, 9.037516e-01,
     1.198578e-01, 3.966083e-01, 1.403837e-02, 7.328671e-01, 6.793476e-02,
     4.040730e-03, 3.033349e-04, 1.125147e-02, 2.375072e-02, 5.818542e-04,
     3.075482e-04, 8.251272e-03, 1.356534e-03, 1.360696e-02, 3.764588e-04,
     1.801145e-05, 2.504456e-07, 3.310253e-02, 9.427839e-03, 8.791153e-04,
     2.177831e-04, 9.693054e-04, 6.610250e-05, 2.900813e-02, 5.735490e-03]

# Benjamini & Yekutieli (bejamini yekutieli)
bhy = [1.000000e+00, 1.000000e+00, 8.940844e-01, 8.510676e-01, 1.000000e+00,
     1.000000e+00, 1.000000e+00, 1.000000e+00, 1.000000e+00, 1.000000e+00,
     1.000000e+00, 1.000000e+00, 1.000000e+00, 1.000000e+00, 1.000000e+00,
     1.000000e+00, 1.000000e+00, 1.000000e+00, 1.000000e+00, 5.114323e-01,
     1.000000e+00, 1.000000e+00, 1.000000e+00, 1.000000e+00, 1.000000e+00,
     1.000000e+00, 1.000000e+00, 1.754486e-01, 1.000000e+00, 6.644618e-01,
     7.575031e-02, 1.153102e-02, 1.581959e-01, 2.812089e-01, 1.636176e-02,
     1.153102e-02, 1.325863e-01, 2.774239e-02, 1.754486e-01, 1.209832e-02,
     2.025930e-03, 5.634031e-05, 3.546073e-01, 1.413926e-01, 2.180552e-02,
     1.153102e-02, 2.180552e-02, 4.956812e-03, 3.262838e-01, 9.925057e-02]
 
# Bonferroni (bonferonni)
b = [1.000000e+00, 1.000000e+00, 1.000000e+00, 1.000000e+00, 1.000000e+00,
    1.000000e+00, 1.000000e+00, 1.000000e+00, 1.000000e+00, 1.000000e+00,
    1.000000e+00, 1.000000e+00, 1.000000e+00, 1.000000e+00, 1.000000e+00,
    1.000000e+00, 1.000000e+00, 1.000000e+00, 1.000000e+00, 1.000000e+00,
    1.000000e+00, 1.000000e+00, 1.000000e+00, 1.000000e+00, 1.000000e+00,
    1.000000e+00, 1.000000e+00, 7.019185e-01, 1.000000e+00, 1.000000e+00,
    2.020365e-01, 1.516674e-02, 5.625735e-01, 1.000000e+00, 2.909271e-02,
    1.537741e-02, 4.125636e-01, 6.782670e-02, 6.803480e-01, 1.882294e-02,
    9.005725e-04, 1.252228e-05, 1.000000e+00, 4.713920e-01, 4.395577e-02,
    1.088915e-02, 4.846527e-02, 3.305125e-03, 1.000000e+00, 2.867745e-01]

# Hochberg (hochberg)
h = [9.991834e-01, 9.991834e-01, 9.991834e-01, 9.991834e-01, 9.991834e-01,
    9.991834e-01, 9.991834e-01, 9.991834e-01, 9.991834e-01, 9.991834e-01,
    9.991834e-01, 9.991834e-01, 9.991834e-01, 9.991834e-01, 9.991834e-01,
    9.991834e-01, 9.991834e-01, 9.991834e-01, 9.991834e-01, 9.991834e-01,
    9.991834e-01, 9.991834e-01, 9.991834e-01, 9.991834e-01, 9.991834e-01,
    9.991834e-01, 9.991834e-01, 4.632662e-01, 9.991834e-01, 9.991834e-01,
    1.575885e-01, 1.383967e-02, 3.938014e-01, 7.600230e-01, 2.501973e-02,
    1.383967e-02, 3.052971e-01, 5.426136e-02, 4.626366e-01, 1.656419e-02,
    8.825610e-04, 1.252228e-05, 9.930759e-01, 3.394022e-01, 3.692284e-02,
    1.023581e-02, 3.974152e-02, 3.172920e-03, 8.992520e-01, 2.179486e-01]

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

def order(*args):
    """
    Order the arguments.
    """
    if len(args) > 1:
        if args[1].lower() == "false":# if ($string1 eq $string2) {
            return sorted(range(len(args[0])), key = lambda k: args[0][k])
        elif list(args[1].lower()) == list("true"):
            return sorted(range(len(args[0])), key = lambda k: args[0][k], reverse = True)
        else:
            print "%s isn't a recognized parameter" % args[1]
            sys.exit()
    elif len(args) == 1:
        return sorted(range(len(args[0])), key = lambda k: args[0][k])
