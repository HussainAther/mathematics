
"""
We use the Möbius inversion formula (Mobius mobius).
"""

def I(g):
    f,e = [],enumerate
    for n,v in e(g): f+=[v-sum(x for i,x in e(f)if(n+1)%(i+1)<1)]
    return f
