import numpy as np

"""
Imagine a pond enclosed by a 2-dimensional box.
We'll use the sampling technique of throwing stones into a pond
as a methof of measuring the area of the pond. The ratio of "hits" to
the total number of stones thrown equals the artio of the area of the pond
to that of the box. We can also determine pi through this method (as described
by Buffon's needle.)
"""

def sample_cosine():
    rr = 2
    while rr > 1.:
      u1 = np.random.uniform(0,1.)
      u2 = np.random.uniform(0,1.)
      v1 = 2*u1-1.
      rr = v1*v1+u2*u2
    cc = (v1*v1-u2*u2)/rr
    return cc

class Buffon_needle_problem:

     def __init__(self,x,y,n,m):
        self.x = float(x)  #width of the needle
        self.y = float(y)  #witdh of the space
        self.r = [] #coordinated of the centre of the needle
        self.z = [] #measure of the alignment of the needle
        self.n = n  #no of throws
        self.m = m  #no of simulations
        self.p = self.x/self.y
        self.pi_approx = []

    def samples(self):
        # throwing the needles
        for i in range(self.n):
            self.r.append(np.random.uniform(0,self.y))
            C=sample_cosine()
            self.z.append(C*self.x/2.)
        return [self.r,self.z]

    def simulation(self):
        # m simulation
        for j in range(self.m):
            self.r=[]
            self.z=[]
            self.samples()
            # n throw
            hits = 0 #setting the success to 0
            for i in range(self.n):
                #condition for a hit
                if self.r[i]+self.z[i]>=self.y or self.r[i]-self.z[i]<0.:
                    hits += 1
                else:
                    continue
            est =self.p*float(self.n)/float(hits)
            self.pi_approx.append(est)
        return self.pi_approx

y = Buffon_needle_problem(1,2,80000,5)

print (y.simulation())
