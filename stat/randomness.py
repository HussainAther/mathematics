
"""
We can define a sequence of numbers as random if there are no correlations among the numbers.
If all the numbres in a sequence are equally likely to occur, it is uniform.
"""
# Power resideue method of generation a psuedo-random sequence of numbers
def next_num(prev, M): # generate the next number in the sequence. prev is the previous number. M is the upper bound of the interval of numbers we can choose from.
    a = 5 # some constant
    c = 6 # another constant lol
    return (a*prev+c) % M

