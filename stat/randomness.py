"""
We can define a sequence of numbers as random if there are no correlations among the numbers.
If all the number in a sequence are equally likely to occur, it is uniform.

Linear congruent (lcg) power residue method of generation a psuedo-random sequence of numbers.
"""

def lcg(prev): # generate the next number in the sequence. prev is the previous number. M is the upper bound of the interval of numbers we can choose from.
    a = 699224 # some constant
    c = 520499118 # another constant lol
    M = 2**24 # max interva
    return (a*prev+c) % M

for i in range(10):
    print lcg()
