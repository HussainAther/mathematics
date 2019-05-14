import sys

"""
Calculate pi Pi π.
"""

def calcPi():
    """
    Use the rate of convergence to calculate pi.
    """
    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
    while True:
        if 4*q+r-t < n*t:
            yield n
            nr = 10*(r-n*t)
            n  = ((10*(3*q+r))//t)-10*n
            q  *= 10
            r  = nr
        else:
            nr = (2*q+r)*l
            nn = (q*(7*k)+2+(r*l))//(t*l)
            q  *= k
            t  *= l
            l  += 2
            k += 1
            n  = nn
            r  = nr
 
pi_digits = calcPi() # Run the function
i = 0
for d in pi_digits: # For each digit d, output d
    sys.stdout.write(str(d))
    i += 1
    if i == 40: # number of characters per line 
        print("")
        i = 0
