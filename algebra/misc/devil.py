import numpy as np
import pylab as plt

"""
Here is a strange continuous function on the unit interval, whose derivative is 0 almost everywhere, but it somehow magically rises from 0 to 1!

Take any number X in the unit interval, and express it in base 3. Chop off the base 3 expansion right after the first 1. Next change all 2's in the expansion to 1's. This number now has only 0's or 1's in its expansion, so we can interpret it as a base 2 number! Call this new number f(x).

If you plot this function, you get something called the Devil's Staircase. It is related to the standard Cantor set in the following way. This function is constant at all the removed intervals from the standard Cantor set. For instance if x is in [1/3,2/3], then f(x)=1/2. If x is in [1/9,2/9], then f(x)=1/4; if x is in [7/9,8/9], then f(x)=3/4.
"""

k=0.15

pb=np.zeros(200)
ppb=np.zeros(200)

def f(b):
    i=0
    x=np.zeros(500)
    x[0]=0.1
    while i < 499:
        x[i+1]=(x[i]+b+k*np.sin(2.*np.pi*x[i]))  
        i=i+1
    return x[499]    

j=0
while j<200:
    pb[j]=f(0.005*j)
    ppb[j]=0.005*j
    j=j+1

plt.plot(ppb,pb/500.0, "k-", linewidth=2)

plt.axis([-0.05,1.05,-0.05,1.05])

plt.ylabel("Rotation number", fontsize=18)
plt.xlabel("b", fontsize=18)


plt.show()
