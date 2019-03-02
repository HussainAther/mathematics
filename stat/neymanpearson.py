
"""
Neyman-Pearson Lemma: Let L(theta|x) denote hte likelihood function for the random variable X corresponding to the
probability measure P_theta. If there exists a critical region C of size alpha and a nonnegative constant
k such that

L(theta1|x)/L(theta0|x) >= k for x in region C and L(theta1|x) <= L(theta0|x) for x not in region C,

then C is the most powerful critical region of size alpha.

If a random sample is taken from a distribution with parameter t, a hypothesis is a simple hypothesis
if the hypothesis uniquely specififes the distribution of the population from which the sample is taken.
Any other hypothesis is a composite hypothesis.

The critical region is the region of values that corresponds to the rejection of the null hypothesis at some chosen probability level.
"""

def neymanPearson(funct, k):
    """
    Return the critical regions for a likelihood function
    """
    cr = [] # critical regions
    for i in range(0, 1, .01):
        for j in range(0, 1, .01):
            c = (i,j) # testing critical region
            if lf(i)/lf(j) >= k or lf(i)/lf(j) <= k:
                brak
        cr.append(c)
    return cr

def lf(prob):
    """
    Return some likelihood function that corresponds to the prob, which is the probability measure for a random variable x.
    """
    if prob <= .5:
        return .5
    elif prob > .5 and <=.75:
        return .25
    else:
        return .1
