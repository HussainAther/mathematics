"""
Here’s a cute coin row game that corresponds to an optimization problem. We have a set
of coins in a row all with positive values. We need to pick a subset of the coins to
maximize their sum, but with the additional constraint that we are not allowed to pick two
adjacent coins.

Given:

14    3    27    4    5    15    1

You should pick 14, skip 3, pick 27, skip 4 and 5, pick 15 and skip 1. This gives a total of
56, which is optimal. Note that alternately picking and skipping coins does not work for
this example (or in general). If we picked 14, 27, 5 and 1, we would only get 47. And if
we picked 3, 4, and 15, we would get a pathetic score of 22.

Can you find the maximum value for the coin row problem below?

3    15    17    23    11   3    4    5    17    23    34    17    18    14    12    15
"""


def coinsVariant(row, table):
    """
    Recursively select coins satisfying the adjacency constraint.
    """

    #Base case: no coins
    if len(row) == 0:
        table[0] = 0
        return 0, table
    #base case: one coin, select it
    elif len(row) == 1:
        table[1] = row[0]
        return row[0], table

    """
    Take the maximum amount and store it. With the
    recursive calls, we can skip, pick the coin and skip the next,
    and pick two coins and skip two coins.
    """
    skip = coinsVariant(row[1:], table)[0]
    pickSkip = coinsVariant(row[2:], table)[0] + row[0]
    pickPick = coinsVariant(row[4:], table)[0] + row[0] + row[1]
    result = max(skip, pickSkip, pickPick)
    table[len(row)] = result
    
    return result, table

def tracebackVariant(row, table):
    """
    Input row of coins and the maximum value of each subproblem
    stored in the dictionary.
    """

    #Tracing back the coin selection
    select = []
